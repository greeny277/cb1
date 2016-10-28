int cnt;


int a1(int p0, int p1) {
    int dummy;
    
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 2) { cnt := cnt + 1; dummy := a1(p1, p0);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int a2(int p0, int p1) {
    int dummy;
    p0 := p0 + 1;
    p1 := p1 + 1;
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 2) { cnt := cnt + 1; dummy := a2(p1, p0);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int f(int p0, int p1, int p2, int p3) {
    int dummy;
    
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 4) { cnt := cnt + 1; dummy := f(p1, p2, p3, p0);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int g(int p0, int p1, int p2, int p3) {
    int dummy;
    p0 := p0 + 1;
    p1 := p1 + 1;
    p2 := p2 + 1;
    p3 := p3 + 1;
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 4) { cnt := cnt + 1; dummy := g(p1, p2, p3, p0);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int fb(int p0, int p1, int p2, int p3) {
    int dummy;
    
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 4) { cnt := cnt + 1; dummy := fb(p3, p0, p1, p2);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int gb(int p0, int p1, int p2, int p3) {
    int dummy;
    p0 := p0 + 1;
    p1 := p1 + 1;
    p2 := p2 + 1;
    p3 := p3 + 1;
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 4) { cnt := cnt + 1; dummy := gb(p3, p0, p1, p2);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int h1(int p0, int p1, int p2, int p3, int p4, int p5, int p6, int p7, int p8, int p9, int p10, int p11, int p12, int p13, int p14, int p15, int p16, int p17, int p18, int p19, int p20, int p21, int p22, int p23, int p24, int p25, int p26, int p27, int p28, int p29, int p30, int p31, int p32, int p33) {
    int dummy;
    
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeInt(p4); dummy := writeChar(32);
    dummy := writeInt(p5); dummy := writeChar(32);
    dummy := writeInt(p6); dummy := writeChar(32);
    dummy := writeInt(p7); dummy := writeChar(32);
    dummy := writeInt(p8); dummy := writeChar(32);
    dummy := writeInt(p9); dummy := writeChar(32);
    dummy := writeInt(p10); dummy := writeChar(32);
    dummy := writeInt(p11); dummy := writeChar(32);
    dummy := writeInt(p12); dummy := writeChar(32);
    dummy := writeInt(p13); dummy := writeChar(32);
    dummy := writeInt(p14); dummy := writeChar(32);
    dummy := writeInt(p15); dummy := writeChar(32);
    dummy := writeInt(p16); dummy := writeChar(32);
    dummy := writeInt(p17); dummy := writeChar(32);
    dummy := writeInt(p18); dummy := writeChar(32);
    dummy := writeInt(p19); dummy := writeChar(32);
    dummy := writeInt(p20); dummy := writeChar(32);
    dummy := writeInt(p21); dummy := writeChar(32);
    dummy := writeInt(p22); dummy := writeChar(32);
    dummy := writeInt(p23); dummy := writeChar(32);
    dummy := writeInt(p24); dummy := writeChar(32);
    dummy := writeInt(p25); dummy := writeChar(32);
    dummy := writeInt(p26); dummy := writeChar(32);
    dummy := writeInt(p27); dummy := writeChar(32);
    dummy := writeInt(p28); dummy := writeChar(32);
    dummy := writeInt(p29); dummy := writeChar(32);
    dummy := writeInt(p30); dummy := writeChar(32);
    dummy := writeInt(p31); dummy := writeChar(32);
    dummy := writeInt(p32); dummy := writeChar(32);
    dummy := writeInt(p33); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 34) { cnt := cnt + 1; dummy := h1(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p0);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeInt(p4); dummy := writeChar(32);
    dummy := writeInt(p5); dummy := writeChar(32);
    dummy := writeInt(p6); dummy := writeChar(32);
    dummy := writeInt(p7); dummy := writeChar(32);
    dummy := writeInt(p8); dummy := writeChar(32);
    dummy := writeInt(p9); dummy := writeChar(32);
    dummy := writeInt(p10); dummy := writeChar(32);
    dummy := writeInt(p11); dummy := writeChar(32);
    dummy := writeInt(p12); dummy := writeChar(32);
    dummy := writeInt(p13); dummy := writeChar(32);
    dummy := writeInt(p14); dummy := writeChar(32);
    dummy := writeInt(p15); dummy := writeChar(32);
    dummy := writeInt(p16); dummy := writeChar(32);
    dummy := writeInt(p17); dummy := writeChar(32);
    dummy := writeInt(p18); dummy := writeChar(32);
    dummy := writeInt(p19); dummy := writeChar(32);
    dummy := writeInt(p20); dummy := writeChar(32);
    dummy := writeInt(p21); dummy := writeChar(32);
    dummy := writeInt(p22); dummy := writeChar(32);
    dummy := writeInt(p23); dummy := writeChar(32);
    dummy := writeInt(p24); dummy := writeChar(32);
    dummy := writeInt(p25); dummy := writeChar(32);
    dummy := writeInt(p26); dummy := writeChar(32);
    dummy := writeInt(p27); dummy := writeChar(32);
    dummy := writeInt(p28); dummy := writeChar(32);
    dummy := writeInt(p29); dummy := writeChar(32);
    dummy := writeInt(p30); dummy := writeChar(32);
    dummy := writeInt(p31); dummy := writeChar(32);
    dummy := writeInt(p32); dummy := writeChar(32);
    dummy := writeInt(p33); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int h2(int p0, int p1, int p2, int p3, int p4, int p5, int p6, int p7, int p8, int p9, int p10, int p11, int p12, int p13, int p14, int p15, int p16, int p17, int p18, int p19, int p20, int p21, int p22, int p23, int p24, int p25, int p26, int p27, int p28, int p29, int p30, int p31, int p32, int p33) {
    int dummy;
    p0 := p0 + 1;
    p1 := p1 + 1;
    p2 := p2 + 1;
    p3 := p3 + 1;
    p4 := p4 + 1;
    p5 := p5 + 1;
    p6 := p6 + 1;
    p7 := p7 + 1;
    p8 := p8 + 1;
    p9 := p9 + 1;
    p10 := p10 + 1;
    p11 := p11 + 1;
    p12 := p12 + 1;
    p13 := p13 + 1;
    p14 := p14 + 1;
    p15 := p15 + 1;
    p16 := p16 + 1;
    p17 := p17 + 1;
    p18 := p18 + 1;
    p19 := p19 + 1;
    p20 := p20 + 1;
    p21 := p21 + 1;
    p22 := p22 + 1;
    p23 := p23 + 1;
    p24 := p24 + 1;
    p25 := p25 + 1;
    p26 := p26 + 1;
    p27 := p27 + 1;
    p28 := p28 + 1;
    p29 := p29 + 1;
    p30 := p30 + 1;
    p31 := p31 + 1;
    p32 := p32 + 1;
    p33 := p33 + 1;
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeInt(p4); dummy := writeChar(32);
    dummy := writeInt(p5); dummy := writeChar(32);
    dummy := writeInt(p6); dummy := writeChar(32);
    dummy := writeInt(p7); dummy := writeChar(32);
    dummy := writeInt(p8); dummy := writeChar(32);
    dummy := writeInt(p9); dummy := writeChar(32);
    dummy := writeInt(p10); dummy := writeChar(32);
    dummy := writeInt(p11); dummy := writeChar(32);
    dummy := writeInt(p12); dummy := writeChar(32);
    dummy := writeInt(p13); dummy := writeChar(32);
    dummy := writeInt(p14); dummy := writeChar(32);
    dummy := writeInt(p15); dummy := writeChar(32);
    dummy := writeInt(p16); dummy := writeChar(32);
    dummy := writeInt(p17); dummy := writeChar(32);
    dummy := writeInt(p18); dummy := writeChar(32);
    dummy := writeInt(p19); dummy := writeChar(32);
    dummy := writeInt(p20); dummy := writeChar(32);
    dummy := writeInt(p21); dummy := writeChar(32);
    dummy := writeInt(p22); dummy := writeChar(32);
    dummy := writeInt(p23); dummy := writeChar(32);
    dummy := writeInt(p24); dummy := writeChar(32);
    dummy := writeInt(p25); dummy := writeChar(32);
    dummy := writeInt(p26); dummy := writeChar(32);
    dummy := writeInt(p27); dummy := writeChar(32);
    dummy := writeInt(p28); dummy := writeChar(32);
    dummy := writeInt(p29); dummy := writeChar(32);
    dummy := writeInt(p30); dummy := writeChar(32);
    dummy := writeInt(p31); dummy := writeChar(32);
    dummy := writeInt(p32); dummy := writeChar(32);
    dummy := writeInt(p33); dummy := writeChar(32);
    dummy := writeChar(10);
    if(cnt < 34) { cnt := cnt + 1; dummy := h2(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30, p31, p32, p33, p0);}
    dummy := writeInt(p0); dummy := writeChar(32);
    dummy := writeInt(p1); dummy := writeChar(32);
    dummy := writeInt(p2); dummy := writeChar(32);
    dummy := writeInt(p3); dummy := writeChar(32);
    dummy := writeInt(p4); dummy := writeChar(32);
    dummy := writeInt(p5); dummy := writeChar(32);
    dummy := writeInt(p6); dummy := writeChar(32);
    dummy := writeInt(p7); dummy := writeChar(32);
    dummy := writeInt(p8); dummy := writeChar(32);
    dummy := writeInt(p9); dummy := writeChar(32);
    dummy := writeInt(p10); dummy := writeChar(32);
    dummy := writeInt(p11); dummy := writeChar(32);
    dummy := writeInt(p12); dummy := writeChar(32);
    dummy := writeInt(p13); dummy := writeChar(32);
    dummy := writeInt(p14); dummy := writeChar(32);
    dummy := writeInt(p15); dummy := writeChar(32);
    dummy := writeInt(p16); dummy := writeChar(32);
    dummy := writeInt(p17); dummy := writeChar(32);
    dummy := writeInt(p18); dummy := writeChar(32);
    dummy := writeInt(p19); dummy := writeChar(32);
    dummy := writeInt(p20); dummy := writeChar(32);
    dummy := writeInt(p21); dummy := writeChar(32);
    dummy := writeInt(p22); dummy := writeChar(32);
    dummy := writeInt(p23); dummy := writeChar(32);
    dummy := writeInt(p24); dummy := writeChar(32);
    dummy := writeInt(p25); dummy := writeChar(32);
    dummy := writeInt(p26); dummy := writeChar(32);
    dummy := writeInt(p27); dummy := writeChar(32);
    dummy := writeInt(p28); dummy := writeChar(32);
    dummy := writeInt(p29); dummy := writeChar(32);
    dummy := writeInt(p30); dummy := writeChar(32);
    dummy := writeInt(p31); dummy := writeChar(32);
    dummy := writeInt(p32); dummy := writeChar(32);
    dummy := writeInt(p33); dummy := writeChar(32);
    dummy := writeChar(10);
    return 0;
}


int main() {
    int dummy;
    cnt := 0;
    dummy := a1(10, 20);
    dummy := writeChar(10);
    cnt := 0;
    dummy := a2(10, 20);
    dummy := writeChar(10);
    cnt := 0;
    dummy := f(1000, 1100, 1200, 1300);
    dummy := writeChar(10);
    cnt := 0;
    dummy := g(1000, 1100, 1200, 1300);
    dummy := writeChar(10);
    cnt := 0;
    dummy := fb(1000, 1100, 1200, 1300);
    dummy := writeChar(10);
    cnt := 0;
    dummy := gb(1000, 1100, 1200, 1300);
    dummy := writeChar(10);
    cnt := 0;
    dummy := h1(1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300);
    dummy := writeChar(10);
    cnt := 0;
    dummy := h2(1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300);
    dummy := writeChar(10);
    return 0;
}

