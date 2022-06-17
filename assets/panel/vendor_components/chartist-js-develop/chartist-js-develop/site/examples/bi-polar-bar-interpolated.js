var data = {
  labels: ['ه1', 'ه2', 'ه3', 'ه4', 'ه5', 'ه6', 'ه7', 'ه8', 'ه9', 'ه10'],
  series: [
    [1, 2, 4, 8, 6, -2, -1, -4, -6, -2]
  ]
};

var options = {
  high: 10,
  low: -10,
  axisX: {
    labelInterpolationFnc: function(value, index) {
      return index % 2 === 0 ? value : null;
    }
  }
};

new Chartist.Bar('.ct-chart', data, options);
