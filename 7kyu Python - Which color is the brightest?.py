def brightest(colors):
    return max(colors, key=lambda c:max(c[1:3], c[3:5], c[5:]))





if __name__ == '__main__':
    assert brightest(["#001000", "#000000"]) == "#001000"
    assert brightest(["#ABCDEF", "#123456"]) == "#ABCDEF"
    assert brightest(["#00FF00", "#FFFF00"]) == "#00FF00"
    assert brightest(["#FFFFFF", "#1234FF"]) == "#FFFFFF"
    assert brightest(["#FFFFFF", "#123456", "#000000"]) == "#FFFFFF"