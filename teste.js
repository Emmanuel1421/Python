try{
    var a=
    ["34","32","5","31","24","44","67"];
    console.log(a);
    console.log(b);
} catch (e) {
    console.log("Mensagem de erro: "+e.message);
}

let num="A";
try{
    if(isNaN(num)) throw "não é um número!"
    else if (num>40) throw "maior que 40,"
    else if (num<=30) throw "Menor que 30."
    else console.log("blz!")
}catch(e){
    console.log(e);
}

var vitor =['val1','val2','val3'];

vitor[20]="texto";

console.log(vitor);



/*
//renato é o homem que mais da a bunda no globo terrestre
//renato é um estudado
//renato é um homem que gosta de dar a bunda
//renato é 
//cavalos...
//a cleide de mini saia bem curtinha
//5 mil cavalos em nicolas
//no matagal 
//coisa boa hein cleide
//ai dalva como voce bebe agua
//eu sou um estudado
//
*///surpresa, eu voltei

var pessoa = ['Josélio','Alberisto','Jonas'];
pessoa.splice(2,0,"Alberto","Joca");
console.log(pessoa);


var novaPessoa = pessoa.slice(1,3);
console.log(novaPessoa);
