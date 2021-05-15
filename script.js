$(document).ready(function () {
  var scroll = new SmoothScroll('a[href*="#"]', {
    speed: 500,
    speedAsDuration: true,
    customEasing: function (time) {
      return time < 0.5 ? 2 * time * time : -1 + (4 - 2 * time) * time;
    },
  });

  $(".open").on("click", function () {
    $(".popup, .popup-content").addClass("active");
  });

  $(".close, .popup").on("click", function () {
    $(".popup, .popup-content").removeClass("active");
  });
});
