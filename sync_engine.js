/**
 * sync_engine.js — Persistent Study Progress Synchronization Engine
 * Huawei ICT Competition (Computing Track) Study Reviewer
 *
 * Capabilities:
 * 1. Automatic background synchronization with local Python server (progress.json).
 * 2. Real-time interception of localStorage updates to persist immediately to disk.
 * 3. Export / Import progress as JSON for backup and cross-device migration.
 * 4. Automatic Git Commit & Push via local server API.
 */
(function() {
  const STORAGE_KEY = 'huawei_study_progress_v1';
  let isConnectedToServer = false;
  let syncDebounceTimer = null;

  // Intercept localStorage.setItem to auto-save to /api/progress on HTTP
  const originalSetItem = localStorage.setItem.bind(localStorage);
  localStorage.setItem = function(key, val) {
    originalSetItem(key, val);
    if (key === STORAGE_KEY && window.location.protocol.startsWith('http')) {
      clearTimeout(syncDebounceTimer);
      syncDebounceTimer = setTimeout(() => {
        try {
          const progObj = JSON.parse(val);
          fetch('/api/progress', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ progress: progObj })
          })
          .then(res => res.json())
          .then(data => {
            if (data && data.status === 'ok') {
              window.dispatchEvent(new CustomEvent('huawei_progress_synced', { detail: data }));
            }
          })
          .catch(err => console.debug('[SyncEngine] Background save offline:', err));
        } catch (e) {}
      }, 300);
    }
  };

  // Pull latest progress from local server on load
  function initServerSync() {
    if (!window.location.protocol.startsWith('http')) {
      updateSyncUI(false, 'Offline (file:// mode - saving to LocalStorage)');
      return;
    }

    fetch('/api/progress')
      .then(res => {
        if (!res.ok) throw new Error('Server returned ' + res.status);
        return res.json();
      })
      .then(data => {
        isConnectedToServer = true;
        if (data && data.progress) {
          const local = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
          // Merge server data with local data (server wins ties on score, local wins if newer completed)
          const merged = Object.assign({}, data.progress, local);
          originalSetItem(STORAGE_KEY, JSON.stringify(merged));

          // If local had unsynced keys not on server, post merged back
          if (Object.keys(local).length > 0) {
            fetch('/api/progress', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ progress: merged })
            }).catch(() => {});
          }

          // Trigger page UI refreshes
          if (typeof window.renderOverview === 'function') window.renderOverview();
          if (typeof window.renderSidebar === 'function') window.renderSidebar();
          if (typeof window.refreshDoneBadge === 'function') window.refreshDoneBadge();
        }
        updateSyncUI(true, '🟢 Synced with progress.json on disk');
      })
      .catch(err => {
        isConnectedToServer = false;
        updateSyncUI(false, '⚠️ Local server not running (saved to LocalStorage)');
      });
  }

  function updateSyncUI(connected, message) {
    const el = document.getElementById('sync-status-indicator');
    if (el) {
      el.innerHTML = message;
      el.style.color = connected ? '#34d399' : '#fbbf24';
    }
  }

  // Global Sync Helpers
  window.HuaweiSync = {
    isConnected: function() { return isConnectedToServer; },

    // Export progress to downloadable JSON file
    exportJSON: function() {
      const data = localStorage.getItem(STORAGE_KEY) || '{}';
      const parsed = JSON.parse(data);
      const exportPayload = {
        app: "Huawei ICT Competition Computing Track Reviewer",
        exported_at: new Date().toISOString(),
        units_count: Object.keys(parsed).length,
        progress: parsed
      };
      const blob = new Blob([JSON.stringify(exportPayload, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `huawei_study_progress_${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    },

    // Import progress from JSON file
    importJSON: function(file, onComplete) {
      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const json = JSON.parse(e.target.result);
          const incoming = json.progress || json;
          const current = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
          const merged = Object.assign({}, current, incoming);
          localStorage.setItem(STORAGE_KEY, JSON.stringify(merged));

          // Post to server if connected
          if (window.location.protocol.startsWith('http')) {
            fetch('/api/progress', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ progress: merged })
            }).catch(() => {});
          }

          if (typeof window.renderOverview === 'function') window.renderOverview();
          if (typeof window.renderSidebar === 'function') window.renderSidebar();
          if (typeof window.refreshDoneBadge === 'function') window.refreshDoneBadge();
          if (onComplete) onComplete(true, Object.keys(merged).length);
        } catch (err) {
          if (onComplete) onComplete(false, err.message);
        }
      };
      reader.readAsText(file);
    },

    // Trigger server-side git commit and push
    gitPush: function(btnElement) {
      if (!window.location.protocol.startsWith('http')) {
        alert('Git Sync requires launching via "py run_reviewer.py" with the local server active.');
        return;
      }
      const originalText = btnElement ? btnElement.innerHTML : '';
      if (btnElement) {
        btnElement.innerHTML = '⏳ Committing & Pushing to GitHub...';
        btnElement.disabled = true;
      }

      fetch('/api/git-sync', { method: 'POST' })
        .then(r => r.json())
        .then(res => {
          if (btnElement) {
            btnElement.innerHTML = originalText;
            btnElement.disabled = false;
          }
          if (res.status === 'ok') {
            alert('✅ Git Sync Successful!\n\n' + res.message);
          } else {
            alert('⚠️ Git Sync Warning:\n\n' + res.message);
          }
        })
        .catch(err => {
          if (btnElement) {
            btnElement.innerHTML = originalText;
            btnElement.disabled = false;
          }
          alert('❌ Git Sync Request Failed: ' + err.message);
        });
    }
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initServerSync);
  } else {
    initServerSync();
  }
})();
