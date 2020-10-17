""" Tests for orf.py """

import os
from subprocess import getstatusoutput

PRG = './orf.py'
INPUT1 = './tests/inputs/1.fa'
INPUT2 = './tests/inputs/2.fa'
INPUT3 = './tests/inputs/3.fa'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Usage """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def run(file, expected):
    """ Run with inputs """

    rv, out = getstatusoutput(f'{PRG} {file}')
    assert rv == 0
    assert set(out.splitlines()) == set(expected)


# --------------------------------------------------
def test_ok1():
    """ OK """

    expected = [
        'M', 'MGMTPRLGLESLLE', 'MLLGSFRLIPKETLIQVAGSSPCNLS', 'MTPRLGLESLLE'
    ]

    run(INPUT1, expected)


# --------------------------------------------------
def test_ok2():
    """ OK """

    expected = [
        'M', 'MAEGGYRTSNHGSSL', 'MAYPRQYVRCLPKW', 'MDARISTTFELPYLTICQAFTF',
        'MDKHKKWTPVFLLPLSCPISLSVRHLHSDG', 'MGLQ', 'MIDL', 'MLEAQTDG',
        'MLWTNTRNGRPYFYYL', 'MPARRPRFLLTQQERRRPAFARLLVVCQTVSLSSGETVECDSG',
        'MPCYGQTQEMDARISTTFELPYLTICQAFTF', 'MPDGFFVQWGNG', 'MPDR', 'MPFC',
        'MPNPEGWVDLVFHAFLLRQAVLGTRLSRRGGYNRKVPIRSSAAPCTSR',
        'MRLSRIALNRFPTGQRNRLAYDK', 'MSEETD', 'MTRMLEAQTDG',
        'MTTQKAGIQWAYNKLLTTAFGVTKLD', 'MVFWYTRR'
    ]

    run(INPUT2, expected)


# --------------------------------------------------
def test_ok3():
    """ OK """

    expected = [
        'M', 'MACLAPRVPVS', 'MAIGVVWV', 'MANGVVATGLGRSLLA', 'MDRRAMAIGVVWV',
        'MKHAFRISFQANNCVWVN', 'MLAGHVGWP', 'MLFSAV', 'MLGGLNYG',
        'MLGYRLHRMRTIPRPRHESL',
        'MLHAHGGWNLRPLDYSQKASWIQILGSLLPVIKATQHVPRASIVLVGLR', 'MLRAY',
        'MNRCRFYIPPEMPTAEGYPHGEGPSTL',
        'MNVLALCYFLRFRTNRRPGGASEVAIDTYYYLHATACRWLLA',
        'MPSVSVFRQTIVCGSTKLLVITMNVLALCYFLRFRTNRRPGGASEVAIDTYYYLHATACRWLLA',
        'MPTAEGYPHGEGPSTL', 'MRMKHAFRISFQANNCVWVN', 'MRMVAGIYDRWIILRRLLGSKS',
        'MRTIPRPRHESL', 'MRVAFCCWHFGGYVKSTTIHVWALV', 'MSGPWYSPHPM',
        'MSIRVNGQRRGSDRIGPLPSCLIL', 'MSREHLLSW', 'MSSTSTLKGCYM',
        'MSWRYAIFCGLERIAAQEERRKLQSILIIICTQPPVDGYWRSLGIAIPRLRQ', 'MTSPEYRTSARA',
        'MVAGIYDRWIILRRLLGSKS',
        'MVITSSLVDPHTIVCLKTDTEGMLHAHGGWNLRPLDYSQKASWIQILGSLLPVIK' +
        'ATQHVPRASIVLVGLR', 'MVKALPPYEYTSKWPTAW'
    ]

    run(INPUT3, expected)
