let domainType = (d) =>
  d.map((e) => {
    switch (e.substring(e.lastIndexOf('.'), e.length)) {
      case '.org':
        return 'organization';
      case '.com':
        return 'commercial';
      case '.net':
        return 'network';
      case '.info':
        return 'information';
    }
  });
console.log(
  domainType(['en.wiki.org', 'codefights.com', 'happy.net', 'code.info']),
);
