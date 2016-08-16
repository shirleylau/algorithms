function Braces(values) {
    return values.map(IsBalanced);
}

function IsBalanced(string) {
    var Y = 'YES';
    var N = 'NO';
    var status = Y;
    var prev = [];

    var i = 0;
    while (status == Y && i < string.length) {
        var curr = string[i];

        if (curr == '{' || curr == '[' || curr == '(') {
            prev.push(curr);
        } else {
            switch(curr) {
                case '}':
                    status = prev.pop() == '{' ? Y : N;
                    break;
                case ']':
                    status = prev.pop() == '[' ? Y : N;
                    break;
                case ')':
                    status = prev.pop() == '(' ? Y : N;
                    break;
                default:
                    status = N;
            }
        }
        i++;
    }

    return prev.length ? N : status;
}

var input = [ "{}[]()", "{[}]}" ];

var output = Braces(input);

console.log('Input: ', input);
console.log('Output: ', output);
