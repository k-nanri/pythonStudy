from click.testing import CliRunner
from click_easy import show_your_birthplace

def test_show_your_birthplace():
    runner = CliRunner()
    result = runner.invoke(show_your_birthplace, input="Kanagawa\nWAHAHA\n")
    assert result.exit_code == 0
    #assert result.output == "出身は？: Kanagawa\n出身校は？: WAHAHA\nbrithplace = Kanagawa\nschoolname = WAHAHA\n"
    outputs = result.output.split('\n')
    assert len(outputs)-1 == 4 # 末尾の改行を除く
    assert outputs[0] == "出身は？: Kanagawa"
    assert outputs[1] == "出身校は？: WAHAHA"
    assert outputs[2] == "brithplace = Kanagawa"
    assert outputs[3] == "schoolname = WAHAHA"
    assert outputs[4] == ""