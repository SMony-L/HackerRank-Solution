int temp = *a;
    *a = *a + *b;  
    *b = abs(*b - temp);