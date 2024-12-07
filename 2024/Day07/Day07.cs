using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day07;

public class Day07 : BaseDay
{
    private readonly char[] OPERATORS_1 = ['+', '*'];
    private readonly char[] OPERATORS_2 = ['+', '*', '|'];
    
    protected override string Part1(string input)
    {
        return Solve(input, OPERATORS_1);
    }

    protected override string Part2(string input)
    {
        return Solve(input, OPERATORS_2);
    }

    protected override string RelativeInputPath => "Day07/input.txt";

    private List<Equation> GetEquations(string input)
    {
        return input
            .SplitLines()
            .Select(line => line.Split(": "))
            .Select(pair => new Equation(ulong.Parse(pair[0]), pair[1].SplitWords().Select(ulong.Parse).ToList()))
            .ToList();
    }

    private ulong Calculate(ulong operand1, ulong operand2, char op)
    {
        return op switch
        {
            '+' => operand1 + operand2,
            '*' => operand1 * operand2,
            '|' => ulong.Parse(operand1 + operand2.ToString()),
            _ => throw new Exception($"Unknown operator {op}")
        };
    }
    
    private string Solve(string input, char[] operators)
    {
        var equations = GetEquations(input);
        var sum = 0ul;
        
        var permutationCache = equations
            .Select(eq => eq.Operands.Count - 1)
            .Distinct()
            .ToDictionary(key => key, key => operators.PermutationsWithRepetition(key).ToList());
        
        Parallel.ForEach(equations, (equation) =>
        {
            var permutations = permutationCache[equation.Operands.Count - 1];
            
            foreach (var permutation in permutations)
            {
                var result = equation.Operands.First();
                
                foreach (var pair in equation.Operands.Skip(1).Zip(permutation))
                {
                    var (operand, op) = pair;
                    result = Calculate(result, operand, op);

                    if (result > equation.Result)
                    {
                        break;
                    }
                }
                
                if (result == equation.Result)
                {
                    Interlocked.Add(ref sum, result);
                    break;
                }
            }
        });

        return sum.ToString();
    }
}