using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day02;

/// <summary>
/// The LINQ is getting ugly.
/// </summary>
public class Day02 : BaseDay
{
    protected override string Part1(string input) => ParseInput(input).Count(IsSafe).ToString();

    protected override string Part2(string input)
    {
        return ParseInput(input)
            .Count(line => Enumerable.Range(0, line.Count)
                                     .Any(ix => IsSafe(line.Copy().RemoveAtFluent(ix))))
            .ToString();
    }

    protected override string RelativeInputPath => "Day02/input.txt";

    private List<List<int>> ParseInput(string input)
    {
        return input.SplitLines()
                    .Where(line => line.Length != 0)
                    .Select(line => line.SplitWords().Select(x => x.ToInt()).ToList())
                    .ToList();
    }

    private bool IsSafe(IList<int> nums)
    {
        var sign = Math.Sign(nums[1] - nums[0]);
        return nums.Take(nums.Count - 1)
                   .Zip(nums.Skip(1), (prev, curr) => curr - prev)
                   .All(diff => Math.Abs(diff) is >= 1 and <= 3 && Math.Sign(diff) == sign);
    }
}