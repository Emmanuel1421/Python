

//1.
let carros=['corsa','fusca','civic','gol bolinha','uno','gol quadrado'];

//2.
console.log(`O tamanho da lista é:${carros.length}`);

//3.
console.log(`O primeiro elemento é ${carros[0]},o ultimo elemento é ${carros.pop()}`);

//4.
carros.shift();
console.log(carros);
carros.unshift("leoMovel");
console.log(carros);

//5.
carros.pop();
console.log(carros);
carros.push("hb20");
console.log(carros);

//6
carros.splice(1,3);
console.log(carros)

//7
carros.splice(1,0,"leoBlox","renatoBlox")
console.log(carros);



//teste 
const points = [40,100,1,5,25,10];
points.sort(function (a,b) {return a-b});
console.log(points);
points.sort(function (a,b) {return b-a});
console.log(points);
points.sort(function () {return 0.5 - Math.random()});
console.log(points);


    
