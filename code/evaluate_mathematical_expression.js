function unpack(string){
  if(string.indexOf('(') === -1) return string

  var prev = ''
  var start = 0
  var end = 0
  for(i=0,l=string.length; i<l; i++){
    char = string[i]
    if(char === '('){
      prev = char
      start = i
    }else if(char === ')'){
      if(prev === '('){
        end = i;
        break;
  }}}

  string = string.split('')
  var inside = calculate(string.splice(start+1, end-start-1).join(''))
  string.splice(start,2, inside)
  return unpack(string.join(''))

}

function isOperation(char){
  if(char==='+' || char==='-' || char==='/' || char=== '*') return true
  return false
}

function calculate(string){
  string = string.split(' ').join('')
  string = string.replace(/--/g, '+').replace(/-\+/g, '-').replace(/\+-/g, '-')
  if(string[0] !== '-' && string[0] !== '+') string = '+' + string

  var res = []
  var first_special = -1
  for(i=0,l=string.length;i<l;i++){
    curr = string[i]
    prev = res[res.length-1]
    if(isOperation(curr) && !isOperation(prev)){
      if(first_special === -1 && (curr === '/' || curr ==='*' )) first_special = res.length
      if(i!==0) res[res.length-1] = parseFloat(prev)
      res.push(curr)
    }else{
      if(res.length>2 && isOperation(prev) && isOperation(res[res.length-2])) res[res.length-1] += curr
      else if(i!==0 && !isOperation(prev)) res[res.length-1] += curr
      else res.push(curr)
    }
    if(i+1===string.length) res[res.length-1] = parseFloat(res[res.length-1])
  }

  var i = first_special === -1? 0 : first_special - 2
  var l = first_special === -1? res.length : first_special + 1
  var sum = 0
  for(; i<l; i+=2){
    switch(res[i]){
      case('+'): sum += res[i+1]; break;
      case('-'): sum -= res[i+1]; break;
      case('/'): sum /= res[i+1]; break;
      case('*'): sum *= res[i+1]; break;
    }
  }

  if(first_special !== -1) res.splice(first_special-2, 4, sum< 0? '':'+',sum)

  return first_special === -1 || res.length <= 2 ? sum : calculate(res.join(''))
}


var calc = function (string) {
  string = unpack(string)
  return calculate(string)
};

const expression = '3 + 3 * 9 -10 * -1 /5 * 7 -80'
console.log(calc(expression) == eval(expression))