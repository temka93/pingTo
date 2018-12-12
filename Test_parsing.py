import Ping


def test_parsingAvr():
    out = Ping.ping()
    #print Ping.parserAvr(out)
    assert int(Ping.parserAvr(out)) < 40


def test_parsingRec():
    out = Ping.ping()
    assert Ping.parserRec(out) != 0



