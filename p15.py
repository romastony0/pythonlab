class students:
    def studetails(self):
        self.rollno = input('Enter the Rollno: ');
        self.name = input('Enter the Rollno: ');
        self.m1 = int(input('Enter the Tamil '));
        self.m2 = int(input('Enter the English: '));
        self.m3 = int(input('Enter the Maths: '));
        self.m4 = int(input('Enter the Science: '));
        self.m5 = int(input('Enter the Social: '));

    def passorfail(self):
        self.total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5;
        self.percentage = self.total / 5;

        if self.percentage >= 35:
            print('PASS', 'Register Number: ', self.rollno, 'Name: ', self.name)
        else:
            print('FAIL', 'Register Number: ', self.rollno, 'Name: ', self.name)

    def average(self):
        print("TOTAL: ", self.total)
        print("AVERAGE: ", self.percentage)




s = students()
s.studetails()

s.passorfail()
s.average()