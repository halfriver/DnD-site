$(document).ready(function() {
  // Set ability score modifiers and progress bar lengths.
  $(".ability-score-mod").each(function() {
    var ability_score = $(this).prev().text();
    var ability_mod = Math.floor(ability_score/2)-5;
    if (ability_mod >= 0) {
      $(this).text("+" + ability_mod);
    } else {
      $(this).text(ability_mod);
    }
    $(this).parent().next().find(".progress-bar").css("width", (ability_score/30)*100+"%")
  });



});
