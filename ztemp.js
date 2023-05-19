// var curry = function (fn) {
//     console.log('entered:')
//     return  function curriedFunc(...args) {
//     if (args.length >= fn.length) {
//       return fn(...args);
//     }
//     return function (...nextArgs) {
//         console.log('...args, ...nextArgs:',...nextArgs )
//       return curriedFunc(...args, ...nextArgs);
//     };
//   }
// };

// function sum(a, b, c,d) { return a + b + c + d; }

// var csum = curry(sum)
// // console.log('csum(1)(2)(3):', csum(1)(2)(3))
// console.log('csum(1,2)(3):', csum(1,2)(3)(4))
//..............................................................................................................

var timeLimit = function(fn, t) {
	return async function(...args) {

      let check1 = new Promise ( reject => setTimeout(()=> { reject("Time Limit Exceeded")}, t))   
      
      let check2 = fn(...args);
        
         return  new Promise.race([check1, check2])
    }
}
