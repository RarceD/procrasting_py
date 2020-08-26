LENGTH = 1200;
HEIGHT =  800;

function setup() {
  createCanvas(LENGTH, HEIGHT);
  player = new Player(123,700);
}
let pos = 10;
let i = 1;
let continueMoving = false;
let value =0 ;
function draw() {
  //I first create the background and flor:
  background(155, 245, 250);
  rect(0, HEIGHT - 100, 529, 55, 20);
  rect(600, HEIGHT - 300, 529, 55, 20);

  rect(pos + i, 100, 10, 100, 100);
  pos += i * 6;
  if (pos > 1200 || pos < 0) i = -i;
  player.draw();
  
  if (player.keepMoving){
    player.move();
  }
  fill(value);
  rect(25, 25, 50, 50);
}

class Player {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.keepMoving = false;
  }
  draw() {
    circle(this.x,this.y, 20);
  }
  move(){
    if (mouseX > LENGTH/2){
      this.x+=10;
    }else{
      this.x-=10;
    }
  }
}
function mousePressed() {
  player.keepMoving = true;
}
function mouseReleased() {
  player.keepMoving = false;
}
function doubleClicked() {
  if (value === 0) {
    value = 255;
    player.y-=100;
  } else {
    value = 0;
    player.y-=100;

    // player.y+=10;

  }
}