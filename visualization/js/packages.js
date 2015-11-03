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
            console.log(node);
            node.parent = find(id.substring(0, i = id.lastIndexOf(".")));
            node.parent.children.push(node);
            node.key = id.substring(i + 1);
          }
        }
        return node;
      }

      classes.forEach(function (d) {
        find(d.name, d);
      });

      return map[""];
    },

    // Return a list of links for the given array of nodes.
    links: function (nodes) {
      var map = {},
          links = [];

      // Compute a map from name to node.
      nodes.forEach(function (d) {
        map[d.name] = d;
      });

      // For each import, construct a link from the source to target node.
      nodes.forEach(function (d) {
        if (d.links) d.links.forEach(function (i) {
          links.push({source: map[d.name], target: map[i]});
        });
      });

      return links;
    }

  };
})();
