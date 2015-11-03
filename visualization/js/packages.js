(function () {
  packages = {

    // Lazily construct the package hierarchy from class names.
    root: function (classes) {
      var map = {};

      function find(id, data) {
        var node = map[id], i;
        if (!node) {
          node = map[id] = data || {id: id, children: []};
          if (id.length) {
            node.parent = find("");
            node.parent.children.push(node);
            node.key = id;
          }
        }
        return node;
      }

      classes.forEach(function (d) {
        find(d.id, d);
      });

      return map[""];
    },

    // Return a list of page_links for the given array of nodes.
    imports: function (nodes) {
      var map = {},
          page_links = [];

      // Compute a map from id to node.
      nodes.forEach(function (d) {
        map[d.id] = d;
      });

      // For each import, construct a link from the source to target node.
      nodes.forEach(function (d) {
        if (d.page_links) d.page_links.forEach(function (i) {
          page_links.push({source: map[d.id], target: map[i]});
        });
      });

      return page_links;
    }

  };
})();
