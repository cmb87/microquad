r = 4.2;
rlx = 80;
rdy = 16;

flx = 18;
fly = 20;

aly = 85;
alx = 6;


cly = 24;
clx = 25;

createArm1 = true;
createArm2 = true;
createFc = true;
createCH=true;

createArm1 = false;
createArm2 = false;
createFc = false;
//createCH=false;
createRails=false;

// Rails
module rails() {
  color("green")
  union(){
    translate([-rlx/2,-r/2+rdy/2,-r])
    cube([rlx,r,r]);
    translate([-rlx/2,-r/2-rdy/2,-r])
    cube([rlx,r,r]);
  };
};

// Flightcontroller
module fcp() {
  color("red")
  difference(){
    union(){
      _bracket(blx=flx);
      translate([-flx/2,-fly/2,0])cube([flx,fly,1]);
      translate([+6.5,+6.5,1])cylinder(r=2,h=2,$fn=20);
      translate([+6.5,-6.5,1])cylinder(r=2,h=2,$fn=20);
      translate([-6.5,+6.5,1])cylinder(r=2,h=2,$fn=20);
      translate([-6.5,-6.5,1])cylinder(r=2,h=2,$fn=20);
    }
    translate([+6.5,+6.5,-1])cylinder(r=0.75,h=20,$fn=20);
    translate([+6.5,-6.5,-1])cylinder(r=0.75,h=20,$fn=20);
    translate([-6.5,+6.5,-1])cylinder(r=0.75,h=20,$fn=20);
    translate([-6.5,-6.5,-1])cylinder(r=0.75,h=20,$fn=20);
  }

}

// Arm
module arms(px=10) {
  color("blue")translate([px,0,0])
  difference(){
      union(){
        translate([-alx/2,-aly/2,0])cube([alx,aly,1]);
        
          
        hull(){
          translate([-alx/2,-aly/2+6,-1])cube([1,1,1]);
          translate([-alx/2,+aly/2-6,-1])cube([1,1,1]);
          translate([-alx/2,-0.5,-4])cube([1,1,4]);
        }
        
        hull(){
          translate([+alx/2-1,-aly/2+6,-1])cube([1,1,1]);
          translate([+alx/2-1,+aly/2-6,-1])cube([1,1,1]);
          translate([+alx/2-1,-0.5,-4])cube([1,1,4]);
        }
        
        translate([0,-aly/2,-1])_platform();
        translate([0,+aly/2,-1])_platform();
        _bracket(blx=alx);
      }
      rails();
      
      translate([0,+aly/2,-10])cylinder(r=1.5,h=20, $fn=30);
      translate([0,-aly/2,-10])cylinder(r=1.5,h=20, $fn=30);
  }
      
}

// CameraHolder
module camera(px=0) {
  color("yellow")translate([px,0,0])

  union(){
    translate([-6,-20/2,0])cube([12,20,15]);
    translate([-6,0,6.5])rotate([0,90,0])cylinder(r=5.5,h=25);

  }
      
}

module cameraHolder(px=0) {
  color("purple")translate([px,0,0])
    
  difference(){
    union(){
      hull(){
        translate([-clx/2+2,-cly/2,-18])cube([3,cly,18]);
        translate([-clx/2+2+20,-0.5*cly/2,-18])cube([3,0.5*cly,2]);
          
        translate([-clx/2+2+15,-0.9*cly/2,-18])cube([3,0.9*cly,2]);  
          
      }
      translate([-clx/2+2.5,0,0])_bracket(blx=7);
      
    }
    
    rails();
    translate([0,0,-16])camera();
    translate([-16,0,-8.5])rotate([0,90,0])cylinder(r=5.5,h=25);
  }
   
}

// bracket
module _bracket(blx=10){
  translate([0,rdy/2,0])
  difference(){
    hull(){
      translate([-blx/2,-(r+2)/2,-r-1])cube([blx,r+2,1]);
      translate([-blx/2,-(r+4)/2,0])cube([blx,r+4,1]);
    }
    translate([-rlx/2,-r/2,-r])
    cube([rlx,r,r]);  }
    
  translate([0,-rdy/2,0])
  difference(){
    hull(){
      translate([-blx/2,-(r+2)/2,-r-1])cube([blx,r+2,1]);
      translate([-blx/2,-(r+4)/2,0])cube([blx,r+4,1]);
    }
    translate([-rlx/2,-r/2,-r])
    cube([rlx,r,r]);  }
    
}


// Plattform
module _platform(mirror=true){
  difference(){
    translate([0,0,0])cylinder(r=7,h=2,$fn=6);
    translate([0,0,-1])cylinder(r=1.5,h=5,$fn=10);
    translate([4.5,0,-1])cylinder(r=0.6,h=5,$fn=10);
    translate([0,4.5,-1])cylinder(r=0.6,h=5,$fn=10);
    translate([-4.5,0,-1])cylinder(r=0.6,h=5,$fn=10);
    translate([0,-4.5,-1])cylinder(r=0.6,h=5,$fn=10);
  }
}






if (createRails){rails();}
if (createArm1){arms(px=20);}
if (createArm2){arms(px=-26);}
if (createFc){fcp();}
if (createCH){cameraHolder(px=60);}
