/**
 * sync_engine.js — Local PC Study Progress Synchronization Engine
 * Huawei ICT Competition (Computing Track) Study Reviewer
 *
 * Guarantees:
 * 1. Progress is saved STRICTLY on this PC (to local progress.json and localStorage).
 * 2. Never pushes to Git, so teammates pulling the repo have their own individual progress.
 * 3. Export / Import progress as JSON for manual personal backup across personal devices.
 */
(function() {
  const STORAGE_KEY = 'huawei_study_progress_v1';
  let isConnectedToServer = false;
  let syncDebounceTimer = null;

  // Intercept localStorage.setItem to auto-save to local progress.json on HTTP
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
              window.dispatchEvent(new CustomEvent('huawei_progress_saved', { detail: data }));
            }
          })
          .catch(err => console.debug('[LocalSync] Offline save:', err));
        } catch (e) {}
      }, 300);
    }
  };

  // Pull latest progress from local server on load
  function initLocalServerSync() {
    if (!window.location.protocol.startsWith('http')) {
      updateSyncUI(false, 'Stored locally in Browser (file:// mode)');
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
          const merged = Object.assign({}, data.progress, local);
          originalSetItem(STORAGE_KEY, JSON.stringify(merged));

          // If local had unsynced keys not on server, write merged back
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
      })
      .catch(err => {
        isConnectedToServer = false;
      });
  }

  // Global Sync & Backup Helpers
  window.HuaweiSync = {
    isConnected: function() { return isConnectedToServer; },

    // Export progress to personal downloadable JSON backup
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
      a.download = `my_personal_study_progress_${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    },

    // Import progress from personal JSON file
    importJSON: function(file, onComplete) {
      const reader = new FileReader();
      reader.onload = function(e) {
        try {
          const json = JSON.parse(e.target.result);
          const incoming = json.progress || json;
          const current = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
          const merged = Object.assign({}, current, incoming);
          localStorage.setItem(STORAGE_KEY, JSON.stringify(merged));

          // Save to local server if running
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

    // Clear personal progress on this device
    resetLocal: function() {
      if (!confirm('Are you sure you want to reset all your study progress on this PC?')) return;
      localStorage.removeItem(STORAGE_KEY);
      if (window.location.protocol.startsWith('http')) {
        fetch('/api/progress', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ progress: {} })
        }).catch(() => {});
      }
      window.location.reload();
    }
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initLocalServerSync);
  } else {
    initLocalServerSync();
  }
})();
