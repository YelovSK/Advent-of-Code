using AoC.Library;
using AoC.Library.Helpers;
using System.Text.RegularExpressions;

namespace AoC.Day03;

public class Day03 : BaseDay
{
    private const string NUM_1 = "num1";
    private const string NUM_2 = "num2";

    private readonly Regex MULT_REGEX = new(@$"mul\((?<{NUM_1}>\d{{1,3}}),(?<{NUM_2}>\d{{1,3}})\)", RegexOptions.Singleline);
    private readonly Regex DONT_REGEX = new(@"don't\(\).*?(do\(\))", RegexOptions.Singleline);

    protected override string Part1(string input) => GetSum(input).ToString();

    protected override string Part2(string input) => GetSum(DONT_REGEX.Replace(input, string.Empty)).ToString();

    protected override string RelativeInputPath => "Day03/input.txt";

    private int GetSum(string input)
    {
        return MULT_REGEX.Matches(input)
                         .Cast<Match>()
                         .Sum(m => m.Groups[NUM_1].Value.ToInt() * m.Groups[NUM_2].Value.ToInt());
    }
}