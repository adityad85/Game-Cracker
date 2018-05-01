class Board(object):
    num_players = 2

    positions = dict(
        ((r, c), 1 << (3 * r + c)) for r in xrange(3) for c in xrange(3))

    inv_positions = dict((v, P) for P, v in positions.iteritems())
    wins = [
        positions[(r, 0)] | positions[(r, 1)] | positions[(r, 2)]
        for r in xrange(3)
    ] + [
        positions[(0, c)] | positions[(1, c)] | positions[(2, c)]
        for c in xrange(3)
    ] + [
        positions[(0, 0)] | positions[(1.1)] | positions[(2, 2)],
        positions[(0, 2)] | positions[(1, 1)] | positions[(2, 0)]
    ]

    def starting_state(self):
        """
        Each of the 9 pairs of player 1 and player 2 board bitmasks 
        plus the win / tie state of the big board for p1 and p2 p;us 
        the row and column of the required board for the next action 
        and finally the player number to move.
        """
        return (0, 0) * 10 + (None, None, 1)

    def display(self, state, action, _unicode=True):
        actions = dict(((R, C, r, c), p) for R in xrange(3) for C in xrange(3)
                       for r in xrange(3) for c in xrange(3)
                       for i, p in enumerate('XO')
                       if state[2 * (3 * R + C) + i] & self.positions[(r, c)])
    player = state[-1]
    sub = u"\u2564".join(u"\u2550" for x in xrange(3))
    top = u"\u2554"+ u"\u2566".join(sub for x in xrange(3)) + u"\u2557\n"
    