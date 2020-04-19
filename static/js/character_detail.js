$(document).ready(function() {
  // Set ability score modifiers and progress bar lengths.
  $(".ability-score-mod").each(function() {
    var ability_score = $(this).prev();
    var ability_mod = Math.floor(ability_score.text()/2)-5;
    if (ability_mod >= 0) {
      $(this).text("+" + ability_mod);
    } else {
      $(this).text(ability_mod);
    }
    if (ability_score.text() == "None") {
      $(this).text("??");
      $(ability_score).text("??");
      $(this).parent().next().find(".progress-bar").css("width", 100+"%").addClass("bg-grey");
    } else {
      $(this).parent().next().find(".progress-bar").css("width", (ability_score.text()/30)*100+"%")
    }

  });
});
