int g ();
void h ( int );
void f () {
    int a ;
    while (1) {
A:        a = g ();
B:        h ( a );
    }
}