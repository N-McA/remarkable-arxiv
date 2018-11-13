
(function () {

  const API_URL = 'http://localhost:8006/get-paper/'


  if (window.location.hostname !== 'arxiv.org') {
    alert('Error: This bookmarklet only works on arxiv.org')
    return;
  }


  const parts = window.location.pathname.split('/');
  const arxivId = parts[parts.length - 1];

  fetch(API_URL + arxivId)
    .then(r => r.json())
    .then(x => {
      alert('Grabbing ' + x.fname)
    })
    .catch(e => alert(e))

})()
