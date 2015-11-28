var w = 600,
h = 600,
rx = w / 2,
ry = h / 2,
m0,
rotate = 0;

var splines = [];

var cluster = d3.layout.cluster()
.size([360, ry - 120])
.sort(function (a, b) { return d3.ascending(a.key, b.key); });

var bundle = d3.layout.bundle();

var line = d3.svg.line.radial()
.interpolate("bundle")
.radius(function (d) { return d.y; })
.angle(function (d) { return d.x / 180 * Math.PI; });

var div = d3.select("body")
  .insert("div")
  .style("position", "absolute")
  .style("top", -80 + "px")
  .style("left", -160 + "px")
  .style("width", w + "px")
  .style("height", h + "px")
  .style("-webkit-backface-visibility", "hidden");

var svg = div.append("svg:svg")
.attr("width", w)
.attr("height", w)
.append("svg:g")
.attr("transform", "translate(" + rx + "," + ry + ")");

svg.append("svg:path")
.attr("class", "arc")
.attr("d", d3.svg.arc().outerRadius(ry - 120).innerRadius(0).startAngle(0).endAngle(2 * Math.PI))
.on("mousedown", mousedown);

d3.json(site_report_filename, function(classes) {
  var nodes = cluster.nodes(packages.root(classes)),
  links = packages.imports(nodes),
  splines = bundle(links);

  var path = svg.selectAll("path.link")
  .data(links)
  .enter().append("svg:path")
  .attr("class", function (d) { return "link source-" + d.source.key + " target-" + d.target.key; })
  .attr("d", function (d, i) {
    if (splines[i].length == 3) {
      return line(splines[i]);
    }
  });

  svg.selectAll("g.node")
  .data(nodes.filter(function (n) { return !n.children; }))
  .enter().append("svg:g")
  .attr("class", function (d) {
    if (d.redirects > 0) {
      console.log(d);
      return "node warning";
    }
    return "node";
  })
  .attr("id", function (d) { return "node-" + d.key; })
  .attr("transform", function (d) { return "rotate(" + (d.x - 90) + ")translate(" + d.y + ")"; })
  .append("svg:text")
  .attr("dx", function (d) { return d.x < 180 ? 8 : -8; })
  .attr("dy", ".31em")
  .attr("text-anchor", function (d) { return d.x < 180 ? "start" : "end"; })
  .attr("transform", function (d) { return d.x < 180 ? null : "rotate(180)"; })
  .text(function (d) { return d.url; })
  .on("mouseover", mouseover)
  .on("mouseout", mouseout);
});

d3.select(window)
.on("mousemove", mousemove)
.on("mouseup", mouseup);

function mouse (e) {
  return [e.pageX - rx, e.pageY - ry];
}

function mousedown () {
  m0 = mouse(d3.event);
  d3.event.preventDefault();
}

function mousemove () {
  if (m0) {
    var m1 = mouse(d3.event),
    dm = Math.atan2(cross(m0, m1), dot(m0, m1)) * 180 / Math.PI;
    div.style("-webkit-transform", "translateY(" + (ry - rx) + "px)rotateZ(" + dm + "deg)translateY(" + (rx - ry) + "px)");
  }
}

function mouseup () {
  if (m0) {
    var m1 = mouse(d3.event),
    dm = Math.atan2(cross(m0, m1), dot(m0, m1)) * 180 / Math.PI;

    rotate += dm;
    if (rotate > 360) rotate -= 360;
    else if (rotate < 0) rotate += 360;
    m0 = null;

    div.style("-webkit-transform", null);

    svg
    .attr("transform", "translate(" + rx + "," + ry + ")rotate(" + rotate + ")")
    .selectAll("g.node text")
    .attr("dx", function (d) { return (d.x + rotate) % 360 < 180 ? 8 : -8; })
    .attr("text-anchor", function (d) { return (d.x + rotate) % 360 < 180 ? "start" : "end"; })
    .attr("transform", function (d) { return (d.x + rotate) % 360 < 180 ? null : "rotate(180)"; });
  }
}

function mouseover (d) {
  svg.selectAll("path.link.target-" + d.key)
  .classed("target", true)
  .each(updateNodes("source", true));

  svg.selectAll("path.link.source-" + d.key)
  .classed("source", true)
  .each(updateNodes("target", true));
}

function mouseout (d) {
  svg.selectAll("path.link.source-" + d.key)
  .classed("source", false)
  .each(updateNodes("target", false));

  svg.selectAll("path.link.target-" + d.key)
  .classed("target", false)
  .each(updateNodes("source", false));
}

function updateNodes (id, value) {
  return function (d) {
    if (value) this.parentNode.appendChild(this);
    svg.select("#node-" + d[id].key).classed(id, value);
  };
}

function cross (a, b) {
  return a[0] * b[1] - a[1] * b[0];
}

function dot (a, b) {
  return a[0] * b[0] + a[1] * b[1];
}
