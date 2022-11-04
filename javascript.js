// union of two array in js
// a = [9, 7, 5]
// b = [1, 2, 3]
// var union = [...new Set([...a, ...b])]
// console.log(union)

//diff of two arrays
// a = [1, 2, 3, 4, 5]
// b = [1, [2], [3, [[4]]],[5,6]]

// function unique(a, b, uniqueArr){
//     for(var i = 0; i < a.length; i++){
//         flag = 0
//         for(var j = 0; j < b.length; j++){
//             if(a[i] == b[j]){
//                 b.splice(j, 1);
//                 j --;
//                 flag = 1
//             }
//         }
//         if(flag == 0){
//             uniqueArr.push(a[i]);
//         }
//     }
//     uniqueArr.push(b)
//     return uniqueArr
// }

// console.log(unique(a, b, []))

