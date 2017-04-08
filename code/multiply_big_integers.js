/*
 * A algorithm to get precise outcome of multiplications
 * where js would only return a result in scientific notation.
 */

function trim_starting_zeros(str){
  res = ''
  for(i=0, l=str.length; i<l; i++){
    if(str[i] !== '0' || res !== '') res = res + str[i]
  }
  return res === '' ? '0' : res
}

function multiply(a, b){
  a = trim_starting_zeros(a)
  b = trim_starting_zeros(b)
  tmp = []
  longest_length = 0
  for(i=0, l = b.length; i<l; i++){
    if(i>0) a = a + '0'
    if(i === b.length - 1) longest_length = a.length
    for(j=0, ll = parseInt(b[b.length-1-i]); j<ll; j++){
      tmp.push(a.split('').reverse().join(''))
    }
  }
  sum = ''
  finished = false
  iteration_number = 0
  //sum up
  //go up the digits
  while(!finished){
    iteration_number++
    row_sum = 0
    for(j=0, ll=tmp.length; j<ll; j++){
      if(0 < tmp[j].length){
        row_sum += parseInt(tmp[j][0])
        tmp[j] = tmp[j].substr(1) || '0'
      }
    }
    row_sum = row_sum.toString().split('').reverse().join('')
    sum += row_sum[0]
    row_sum = row_sum.substr(1)
    if(row_sum !== '') tmp.push(row_sum)
    if(row_sum === '' && iteration_number > longest_length) finished = true

  }
  return trim_starting_zeros(sum.split('').reverse().join(''))
}

console.log(1020303004875647366210 * 2774537626200857473632627613)
console.log(multiply("1020303004875647366210", "2774537626200857473632627613") === "2830869077153280552556547081187254342445169156730")