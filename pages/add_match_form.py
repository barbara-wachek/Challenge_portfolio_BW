from pages.base_page import BasePage

class AddMatchForm(BasePage):
    my_team_field_xpath = "//*[@name='myTeam']"
    enemy_team_field_xpath = "//*[@name='enemyTeam']"
    my_team_score_field_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//*[@name='enemyTeamScore']"
    date_field_xpath = "//*[@name='date']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//form/div[3]/button[2]"
    match_at_home_radio_button_xpath = "//label[@type='radio'][1]"
    match_out_home_radio_button_xpath = "//label[@type='radio'][2]"
    tshirt_color_field_xpath = "//*[@name='tshirt']"
    number_field_xpath = "//*[@name='number']"
    league_field_xpath = "//*[@name='league']"
    time_played_field_xpath = "//*[@name='timePlayed']"
    web_match_field_xpath = "//*[@name='webMatch']"
    general_field_xpath = "//*[@name='general']"
    rating_field_xpath = "//*[@name='rating']"
    pass