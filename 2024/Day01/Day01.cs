using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day01;

public class Day01 : BaseDay
{
    protected override string Part1(string input)
    {
        var lr = GetLeftRight(input);

        var left = lr.Select(lr => lr.Left).Order();
        var right = lr.Select(lr => lr.Right).Order();

        return left.Zip(right, (l, r) => Math.Abs(l - r))
                   .Sum()
                   .ToString();
    }

    protected override string Part2(string input)
    {
        var lr = GetLeftRight(input);

        var left = lr.Select(lr => lr.Left).ToArray();
        var right = lr.Select(lr => lr.Right).ToCounter();

        return left.Sum(l => right.GetValueOrDefault(l, 0) * l)
                   .ToString();
    }

    protected override string RelativeInputPath => "Day01/input.txt";

    private (int Left, int Right)[] GetLeftRight(string input) => input
            .SplitLines()
            .Select(line => line.SplitWords())
            .Select(words => (words.First().ToInt(), words.Last().ToInt()))
            .ToArray();
}