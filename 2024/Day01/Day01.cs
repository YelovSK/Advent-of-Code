using AoC.Library;

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

        var left = lr.Select(lr => lr.Left).ToList();
        var right = lr.Select(lr => lr.Right).ToList();

        return left.Sum(l => right.Count(r => r == l) * l)
                   .ToString();
    }

    protected override string RelativeInputPath => "Day01/input.txt";

    private List<LeftRight> GetLeftRight(string input) => input
            .Split(Environment.NewLine)
            .Select(line => line.Trim().Split(" "))
            .Select(words => new LeftRight(int.Parse(words.First()), int.Parse(words.Last())))
            .ToList();

    private record LeftRight(int Left, int Right); 
}