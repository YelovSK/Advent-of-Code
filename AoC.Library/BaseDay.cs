using AoC.Library.Helpers;

namespace AoC.Library;

public abstract class BaseDay
{
    private readonly string _input;
    
    protected BaseDay()
    {
        _input = File.ReadAllText(InputPath);
    }
    
    public string Part1() => Part1(_input);
    public string Part2() => Part2(_input);
    
    /// <summary>
    /// E.g. 'Day01/input.txt'
    /// </summary>
    protected abstract string RelativeInputPath { get; }
    protected abstract string Part1(string input);
    protected abstract string Part2(string input);
    
    private string InputPath => Path.Combine(PathUtils.GetBaseDirectory(), RelativeInputPath);
}