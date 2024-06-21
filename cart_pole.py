G: float = 9.81
PI: float = 3.14


class CartPole:
    """
    A simple representation of a cart-pole system, often used in control theory and physics.

    The cart-pole system consists of a cart of mass M, which can move horizontally,
    and a pole of mass m attached by an un-actuated joint to the cart. The pole,
    of length l, attempts to balance upright while the cart is influenced by a force F.

    Attributes:
        F (float): Horizontal force applied to the cart (default is 10.0).
        M (float): Mass of the cart (default is 1.0).
        m (float): Mass of the pole (default is 0.1).
        l (float): Length of the pole from its pivot point (default is 1.0).
    """
    def __init__(
        self, *, F: float = 10.0, M: float = 1.0, m: float = 0.1, l: float = 1.0
    ):
        self.F = F
        self.M = M
        self.m = m
        self.l = l

    def print(self):
        print(f"F: {self.F}, M: {self.M}, m: {self.m}, l: {self.l}")