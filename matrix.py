# Matrix row operations calculator
# Darrell Harriman  harrimand@gmail.com 

class Mat:
    """Perform matrix row operations on an n x n list """
    def __init__(self, mtrx):
        """Create object from n x n list

        Args:
            mtrx (2D list of [int|float]): n x n list of integers or floats
        """
        self.update(mtrx)
        self.prec = 3
        self.autoShow = True

    def showRows(self):
        """Display labeled rows of matrix without formatting to set precision

        Args:
            none
        """
        for i, m in enumerate(self.M):
            print("\tRow " + str(i+1) + ": ", self.M[i])
        print("\n")

    def setAutoShow(self, ashow=True):
        """Automatically display matrix after row operations

        Args:
            ashow(boolean): if True, display matrix after row operations
        """
        print("Setting autoShow to ", self.autoShow)
        self.autoShow = ashow

    def R(self, r):
        """Get row from 2D List

        Args:
            r (int): Row number 1 .. len(list)
        """
        if r >= 1 and r <= len(self.M):
            return self.M[r-1]

    def augmentI(self):
        """Augment Matrix with len(list) by len(list) Identity Matrix

        Args:
            none
        """
        L = len(self.M)
        print("Augmenting Matrix with " + str(L) + " x " + str(L) + " Identity Matrix")
        N = []
        for i, m in enumerate(self.M):
            for j, n in enumerate(m):
                m[j] = n * 1.0
            N.extend([m + [0.0 if not(i == ind) else 1.0 for ind in range(L)]])
        self.update(N)
        if self.autoShow: self.show()

    def update(self, mtrx):
        """Update object with calculated mtrx

        Args:
            mtrx (2D list of [int|float]): n x n list of integers or floats
        """
        self.M = mtrx

    def addRows(self, rx, tx, con=1):
        """Add row or a multiple of a row to another row

        Args:
            rx(int): row to be updated with sum of row plus multiple
                of another row.
            tx(int): row to be multiplied by a constant and added to row(rx)
            con([int|float]):  integer or float multiplicand for tx
        """
        if rx >= 1 and rx <= len(self.M) and tx >= 1 and tx <= len(self.M):
            print("Adding " + ((str(con) + " * ") if con != 1 else "")
                  + "Row " + str(tx) + " to Row " + str(rx))
            N = []
            for i, m in enumerate(self.M):
                if i == rx - 1:
                    N.extend([[x+y * con for x, y in zip(self.M[i], self.M[tx - 1])]])
                else:
                    N.extend([m])
            self.update(N)
            if self.autoShow: self.show()
        else: pass


    def subRows(self, rx, tx, con=1):
        """Subtract row or a multiple of a row from another row

        Args:
            rx(int): row to be updated with row minus a multiple
                of another row.
            tx(int): row to be multiplied by a constant and subtracted from row(rx)
            con([int|float]):  integer or float multiplicand for tx
        """
        if rx >= 1 and rx <= len(self.M) and tx >= 1 and tx <= len(self.M):
            print("Subtracting " + ((str(con) + " * ") if con != 1 else "")
                  + "Row " + str(tx) + " from Row " + str(rx))
            N = []
            for i, m in enumerate(self.M):
                if i == rx - 1:
                    N.extend([[x - (y * con) for x, y in zip(self.M[i], self.M[tx - 1])]])
                else:
                    N.extend([m])
            self.update(N)
            if self.autoShow: self.show()
        else: pass

    def mulRow(self, rx, con=1):
        """Multiply row by a constant

        Args:
            rx(int): row to be updated with product of itself and a constant
            con([int|float]):  integer or float multiplicand for rx
        """
        print("Multiplying Row " + str(rx) + " by " + str(con))
        N = []
        for i, m in enumerate(self.M):
            if i == rx - 1:
                N.extend([[x * con for x in self.M[i]]])
            else:
                N.extend([m])
        self.update(N)
        if self.autoShow: self.show()

    def divRow(self, rx, con=1):
        """Divide row by a constant

        Args:
            rx(int): row to be updated with quotient of itself and a constant
            con([int|float]):  integer or float divisor for rx
        """
        print("Dividing Row " + str(rx) + " by " + str(con))
        N = []
        for i, m in enumerate(self.M):
            if i == rx - 1:
                N.extend([[x / con for x in self.M[i]]])
            else:
                N.extend([m])
        self.update(N)
        if self.autoShow: self.show()

    def swapRows(self, rX, rY):
        """Exchange row rX with row rY

        Args:
            rx(int): row to be swapped with row rY
            rY(int): row to be swapped with row rX
        """
        print("Swapping Row " + str(rX) + " with Row " + str(rY))
        N = []
        for i, m in enumerate(self.M):
            if i == rX - 1:
                N.extend([[x for x in self.M[rY-1]]])
            elif i == rY - 1:
                N.extend([[x for x in self.M[rX-1]]])
            else:
                N.extend([m])
        self.update(N)
        if self.autoShow: self.show()

    def subMatrixRight(self):
        """Replace Matrix with right half of matrix

        Args:
            none
        """
        N = []
        for m in self.M:
            N.extend([m[int(len(m)/2):]])
        self.update(N)
        if self.autoShow: self.show()

    def setPrecision(self, P=3):
        """Set displayed precision of elements in m matrix.

        Args:
            P([int]) Number of digits following decimal point.
                If left blank, sets precision to 3 digits
        """
        print("Setting display precision to ", str(P))
        self.prec = P
        if self.autoShow: self.show()

    def show(self):
        """Print Matrix (values formated with set precision)

        Args:
            none
        """
        formatStr = '{:' + str(8) + '.' + str(self.prec) + 'f}'
        for i, m in enumerate(self.M):
            print("|", end="")
            for n in m:
                print(" " if (self.prec > 4) else "", end="")
                print(formatStr.format(n if not(n == 0.0) else 0.0),end="")
            print("  |")
        print("\n")

    def get(self):
        """Returns 2D list populated with matrix values

        Args:
            none
        """
        return self.M

    def help(self):
        print("\n\
        R(r) Get row from 2D List\n\
        augmentI() Augment with len(list) by len(list) Identity Matrix\n\
        swapRows(rX, rY) Exchange row rX with row rY\n\
        addRows(rx, tx, [con=1]) Add (row tx * con) to row rx\n\
        subRows(rx, tx, [con=1]) Subtract (row tx * con) from row rx\n\
        mulRow(rx, [con=1]) Multiply row rx by a constant\n\
        divRow(rx, [con=1]) Divide row rx by a constant\n\
        show() Print Matrix (values formated with set precision)\n\
        showRows() Display labeled rows of matrix without formatting\n\
        setAutoShow([True|False]) Automatic display after row operations\n\
        setPrecision([P=3]) Set displayed precision of elements in matrix.\n\
        subMatrixRight() Replace Matrix with right half of matrix\n\
        get() Returns 2d list populated with matrix values")

