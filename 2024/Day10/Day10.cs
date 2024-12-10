using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day10;

public class Day10 : BaseDay
{
    private const int START = 0;
    private const int END = 9;
    private const int GRADIENT = 1;
    
    protected override string Part1(string input)
    {
        var graph = GetGraph(input);
        var vertices = graph.GetAllVertices();
        var score = 0;
        
        foreach (var start in vertices.Where(v => v.Value == START))
        {
            foreach (var end in vertices.Where(v => v.Value == END))
            {
                score += graph.GetPaths(start, end).Any().ToInt();
            }
        }

        return score.ToString();
    }

    protected override string Part2(string input)
    {
        var graph = GetGraph(input);
        var vertices = graph.GetAllVertices();
        var score = 0;
        
        foreach (var start in vertices.Where(v => v.Value == START))
        {
            foreach (var end in vertices.Where(v => v.Value == END))
            {
                score += graph.GetPaths(start, end).Count();
            }
        }

        return score.ToString();
    }

    protected override string RelativeInputPath => "Day10/input.txt";

    private Graph<int> GetGraph(string input)
    {
        var graph = new Graph<int>();
        var lines = input.SplitLines().ToList();
        
        for (var y = 0; y < lines.Count; y++)
        {
            for (var x = 0; x < lines[y].Length; x++)
            {
                foreach (var (dx, dy) in new[] { (-1, 0), (1, 0), (0, -1), (0, 1) })
                {
                    try
                    {
                        var c1 = lines[y][x].ToInt();
                        var c2 = lines[y + dy][x + dx].ToInt();
                        
                        var v1 = new Vertex<int>(c1, HashCode.Combine(x, y));
                        var v2 = new Vertex<int>(c2, HashCode.Combine(x + dx, y + dy));
                        
                        var diff = c2 - c1;
                        switch (diff)
                        {
                            case GRADIENT:
                                graph.AddEdge(v1, v2);
                                break;
                            case -GRADIENT:
                                graph.AddEdge(v2, v1);
                                break;
                        }
                    }
                    catch
                    {
                        // Imagine unironically checking the bounds
                    }
                }
            } 
        }

        return graph;
    }
}