#============== recursive ==================#
pcoins = [2, 3, 7]
amount = 15


def pcoin(amount, pcoins):
    def _pcoin(amount, pcoins):
        if amount == 0:
            return 0
        elif amount < 0:
            return float("inf")
        else:
            min_coin = min([1 + _pcoin(amount - i, pcoins) for i in pcoins])
        return min_coin

    min_coin = _pcoin(amount, pcoins)
    return min_coin if min_coin != float("inf") else -1


print(pcoin(amount, pcoins))
