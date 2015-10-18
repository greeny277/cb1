
int[3][3] f;
int bi;
int bj;



int win()
{
    int i;
    i:=0;
    while(i<3){
        if(f[i][0]=1&&f[i][1]=1&&f[i][2]=1) {return(1);}
        if(f[i][0]=0-1&&f[i][1]=0-1&&f[i][2]=0-1) {return(0-1);}
        if(f[0][i]=1&&f[1][i]=1&&f[2][i]=1) {return(1);}
        if(f[0][i]=0-1&&f[1][i]=0-1&&f[2][i]=0-1) {return(0-1);}
	i:=i+1;
    }
    if(f[0][0]=1&&f[1][1]=1&&f[2][2]=1) {return(1);}
    if(f[0][0]=0-1&&f[1][1]=0-1&&f[2][2]=0-1) {return(0-1);}
    if(f[0][2]=1&&f[1][1]=1&&f[2][0]=1) {return(1);}
    if(f[0][2]=0-1&&f[1][1]=0-1&&f[2][0]=0-1) {return(0-1);}
    return(0);
}

int printfield()
{
    int i;int j;int dummy;
    i:=0;
    while(i<3){
        dummy:=writeInt(i+1);
	j:=0;
        while(j<3){
	    dummy:=writeChar(124);
            if(f[i][j]=1){
              dummy:=writeChar(88);
            }else{
              if(f[i][j]=0-1){
                dummy:=writeChar(79);
              }else{
                dummy:=writeChar(32);
              }
           }
	   j:=j+1;
        }
	i:=i+1;
dummy:=writeChar(124);
dummy:=writeChar(10);
dummy:=writeChar(32);
dummy:=writeChar(45);
dummy:=writeChar(45);
dummy:=writeChar(45);
dummy:=writeChar(45);
dummy:=writeChar(45);
dummy:=writeChar(45);
dummy:=writeChar(45);
dummy:=writeChar(10);
    }
dummy:=writeChar(32);
dummy:=writeChar(32);
dummy:=writeChar(49);
dummy:=writeChar(32);
dummy:=writeChar(50);
dummy:=writeChar(32);
dummy:=writeChar(51);
dummy:=writeChar(10);
return 0;
}

int rek(int t)
{
    int i;int j;int z;int bw; int w;int s;
    z:=0;
    w:=win(); if(w!=0) {return(w);}
    if(t-t/2*2=1) {s:=0-1;} else {s:=1;}
    bw:=0-s;
    i:=0;
    while(i<3){
        j:=0;
        while(j<3){
            if(f[i][j]=0){
                z:=1; f[i][j]:=s;
                w:=rek(t+1);
                if((w>=bw&&s=1)||(w<=bw&&s=0-1)){
                    bw:=w;
                    if(t=0) {bi:=i;bj:=j;}
                    if(bw=s) {f[i][j]:=0;return(bw);}
                }
                f[i][j]:=0;
            }
	    j:=j+1;
        }
	i:=i+1;
    }
    if(z=0) {bw:=win();}
    return(bw);
}


int main()
{
    int dummy;int i;int j;int w;int amzug;int zug;
    i:=0;
    while(i<3){
      j:=0;
      while(j<3){
        f[i][j]:=0;
	j:=j+1;
      }
      i:=i+1;
    }
dummy:=writeChar(68);
dummy:=writeChar(97);
dummy:=writeChar(114);
dummy:=writeChar(102);
dummy:=writeChar(32);
dummy:=writeChar(105);
dummy:=writeChar(99);
dummy:=writeChar(104);
dummy:=writeChar(32);
dummy:=writeChar(97);
dummy:=writeChar(110);
dummy:=writeChar(102);
dummy:=writeChar(97);
dummy:=writeChar(110);
dummy:=writeChar(103);
dummy:=writeChar(101);
dummy:=writeChar(110);
dummy:=writeChar(32);
dummy:=writeChar(40);
dummy:=writeChar(106);
dummy:=writeChar(47);
dummy:=writeChar(110);
dummy:=writeChar(41);
dummy:=writeChar(63);
dummy:=writeChar(10);
    if(readChar()!=110){
       amzug:=1;
    }else{
       amzug:=0;
    }

    zug:=0;
    dummy:=printfield();

    while(1=1){
        bi:=4;bj:=4;
        zug:=zug+1;
        if(zug>9){
	   dummy:=writeChar(85);
	   dummy:=writeChar(110);
	   dummy:=writeChar(101);
	   dummy:=writeChar(110);
	   dummy:=writeChar(116);
	   dummy:=writeChar(115);
	   dummy:=writeChar(99);
	   dummy:=writeChar(104);
	   dummy:=writeChar(105);
	   dummy:=writeChar(101);
	   dummy:=writeChar(100);
	   dummy:=writeChar(101);
	   dummy:=writeChar(110);
	   dummy:=writeChar(10);
	   return 0;        
	}
	w:=win();
        if(w!=0){
            if(w>0){
	       dummy:=writeChar(73);
	       dummy:=writeChar(99);
	       dummy:=writeChar(104);
	       dummy:=writeChar(32);
	       dummy:=writeChar(104);
	       dummy:=writeChar(97);
	       dummy:=writeChar(98);
	       dummy:=writeChar(101);
	       dummy:=writeChar(32);
	       dummy:=writeChar(103);
	       dummy:=writeChar(101);
	       dummy:=writeChar(119);
	       dummy:=writeChar(111);
	       dummy:=writeChar(110);
	       dummy:=writeChar(110);
	       dummy:=writeChar(101);
	       dummy:=writeChar(110);
	       dummy:=writeChar(10);
	       return 0;
	    }else{
	       dummy:=writeChar(83);
	       dummy:=writeChar(105);
	       dummy:=writeChar(101);
	       dummy:=writeChar(32);
	       dummy:=writeChar(104);
	       dummy:=writeChar(97);
	       dummy:=writeChar(98);
	       dummy:=writeChar(101);
	       dummy:=writeChar(110);
	       dummy:=writeChar(32);
	       dummy:=writeChar(103);
	       dummy:=writeChar(101);
	       dummy:=writeChar(119);
	       dummy:=writeChar(111);
	       dummy:=writeChar(110);
	       dummy:=writeChar(110);
	       dummy:=writeChar(101);
	       dummy:=writeChar(110);
	       dummy:=writeChar(44);
	       dummy:=writeChar(32);
	       dummy:=writeChar(100);
	       dummy:=writeChar(97);
	       dummy:=writeChar(115);
	       dummy:=writeChar(32);
	       dummy:=writeChar(100);
	       dummy:=writeChar(97);
	       dummy:=writeChar(114);
	       dummy:=writeChar(102);
	       dummy:=writeChar(32);
	       dummy:=writeChar(110);
	       dummy:=writeChar(105);
	       dummy:=writeChar(99);
	       dummy:=writeChar(104);
	       dummy:=writeChar(116);
	       dummy:=writeChar(32);
	       dummy:=writeChar(115);
	       dummy:=writeChar(101);
	       dummy:=writeChar(105);
	       dummy:=writeChar(110);
	       dummy:=writeChar(33);
	       dummy:=writeChar(10);
	       return 0;
	   }
        }
        if(amzug!=0){
            if(zug>1) {w:=rek(0);} else {w:=0;bi:=1;bj:=1;}
	    dummy:=writeChar(73);
	    dummy:=writeChar(99);
	    dummy:=writeChar(104);
	    dummy:=writeChar(32);
	    dummy:=writeChar(115);
	    dummy:=writeChar(101);
	    dummy:=writeChar(116);
	    dummy:=writeChar(122);
	    dummy:=writeChar(101);
	    dummy:=writeChar(32);
	    dummy:=writeChar(97);
	    dummy:=writeChar(117);
	    dummy:=writeChar(102);
	    dummy:=writeChar(32);
	    dummy:=writeInt(bi+1);
	    dummy:=writeChar(44);
	    dummy:=writeInt(bj+1);
	    dummy:=writeChar(10);
            f[bi][bj]:=1;
            if(w!=0&&zug<9){
	       dummy:=writeChar(85);
	       dummy:=writeChar(110);
	       dummy:=writeChar(100);
	       dummy:=writeChar(32);
	       dummy:=writeChar(119);
	       dummy:=writeChar(101);
	       dummy:=writeChar(114);
	       dummy:=writeChar(100);
	       dummy:=writeChar(101);
	       dummy:=writeChar(32);
	       dummy:=writeChar(103);
	       dummy:=writeChar(101);
	       dummy:=writeChar(119);
	       dummy:=writeChar(105);
	       dummy:=writeChar(110);
	       dummy:=writeChar(110);
	       dummy:=writeChar(101);
	       dummy:=writeChar(110);
	       dummy:=writeChar(10);
            }
        }else{
            while(bi<1||bi>3||bj<1||bj>3||f[bi-1][bj-1]!=0){
	        dummy:=writeChar(73);
		dummy:=writeChar(104);
		dummy:=writeChar(114);
		dummy:=writeChar(32);
		dummy:=writeChar(90);
		dummy:=writeChar(117);
		dummy:=writeChar(103);
		dummy:=writeChar(32);
		dummy:=writeChar(40);
		dummy:=writeChar(120);
		dummy:=writeChar(32);
		dummy:=writeChar(121);
		dummy:=writeChar(41);
		dummy:=writeChar(58);
		dummy:=writeChar(32);
                bj:=readInt();
		bi:=readInt();
            }
            f[bi-1][bj-1]:=0-1;
        }
        dummy:=printfield();
        amzug:=1-amzug;
    }
    return 0;
}

