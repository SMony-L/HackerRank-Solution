#include <iostream>
#include <stdlib.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions :
class Box {
    private:
        int l, b, h;
    public:
        // Constructors: 
        // Box();
        Box(): l(0), b(0), h(0) {}
        // Box(int,int,int);
        Box(int length, int breadth, int height) {
            l = length;
            b = breadth;
            h = height;
        }
        // Box(Box);
        // Copy Constructor
        Box(const Box &temp) {
            l = temp.l;
            b = temp.b;
            h = temp.h;
        }
        // int getLength(); // Return box's length
        int getLength() {return l;}
        // int getBreadth (); // Return box's breadth
        int getBreadth() {return b;}
        // int getHeight ();  //Return box's height
        int getHeight() {return h;}
        // long long CalculateVolume(); // Return the volume of the box
        long long CalculateVolume() {
            return (long long)l * b * h;
        }
        //Overload operator < as specified
        //bool operator<(Box& b)
        friend bool operator <(Box &A, Box &B) {
            if((A.l < B.l) || ((A.b < B.b) && (A.l == B.l)) || ((A.h < B.h) && (A.l == B.l) && (A.b == B.b))) { 
                return true;
            } else {
                return false;
            }
        };
        //Overload operator << as specified
        //ostream& operator<<(ostream& out, Box& B)
        friend ostream& operator<< (ostream& output, const Box &B) {
            output << B.l << " " << B.b << " " << B.h;
            return output;
        };
        
};

int main() {
    Box b1; // Should set b1.l = b1.b = b1.h = 0;
    Box b2(2, 3, 4); // Should set b1.l = 2, b1.b = 3, b1.h = 4;
    b2.getLength();	// Should return 2
    b2.getBreadth(); // Should return 3
    b2.getHeight();	// Should return 4
    b2.CalculateVolume(); // Should return 24
    cout << b2.CalculateVolume() << endl;
    bool x = (b1 < b2);	// Should return true based on the conditions given
    cout<<b2; // Should print 2 3 4 in order.

    return 0;
}
