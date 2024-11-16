using CommandLine;

namespace AoC.CliOptions;

[Verb("solve", HelpText = "Run a specific day's solution.")]
public class SolveOptions
{
    [Option('d', "day", HelpText = "Day to run. Defaults to the latest day.")]
    public int? Day { get; set; }

    [Option('p', "part1", Default = true, HelpText = "Run Part 1.")]
    public bool Part1 { get; set; }

    [Option('q', "part2", Default = true, HelpText = "Run Part 2.")]
    public bool Part2 { get; set; }
}