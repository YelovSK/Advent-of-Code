using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day08;

// Kind of ugly.. idc
public class Day08 : BaseDay
{
    protected override string Part1(string input)
    {
        var grid = ParseInput(input);
        var antinodes = new HashSet<Position>();
        
        foreach (var kvp in grid.Frequencies)
        {
            var (_, positions) = kvp;
            
            for (var i = 0; i < positions.Count - 1; i++)
            {
                for (var j = i + 1; j < positions.Count; j++)
                {
                    var (p1, p2) = (positions[i], positions[j]);
                    
                    var dx = p1.X - p2.X;
                    var dy = p1.Y - p2.Y;
                    
                    var p3 = new Position(p1.X + dx, p1.Y + dy);
                    var p4 = new Position(p2.X - dx, p2.Y - dy);
                    
                    if (GridHelper.IsInBounds(p3, grid.Size))
                    {
                        antinodes.Add(p3);
                    }
                    if (GridHelper.IsInBounds(p4, grid.Size))
                    {
                        antinodes.Add(p4);
                    }
                }
            }
        }

        return antinodes.Count.ToString();
    }

    protected override string Part2(string input)
    {
        var grid = ParseInput(input);
        var antinodes = new HashSet<Position>();
        
        foreach (var kvp in grid.Frequencies)
        {
            var (_, positions) = kvp;
            for (var i = 0; i < positions.Count - 1; i++)
            {
                for (var j = i + 1; j < positions.Count; j++)
                {
                    var (p1, p2) = (positions[i], positions[j]);
                    antinodes.Add(p1);
                    antinodes.Add(p2);
                    
                    var dx = p1.X - p2.X;
                    var dy = p1.Y - p2.Y;
                    
                    var p3 = new Position(p1.X + dx, p1.Y + dy);
                    var p4 = new Position(p2.X - dx, p2.Y - dy);
                    
                    while (GridHelper.IsInBounds(p3, grid.Size))
                    {
                        antinodes.Add(p3);
                        p3 = new Position(p3.X + dx, p3.Y + dy);
                    }
                    
                    while (GridHelper.IsInBounds(p4, grid.Size))
                    {
                        antinodes.Add(p4);
                        p4 = new Position(p4.X - dx, p4.Y - dy);
                    }
                }
            }
        }

        return antinodes.Count.ToString();
    }

    protected override string RelativeInputPath => "Day08/input.txt";

    private Grid ParseInput(string input)
    {
        var frequencies = input.GetGridPositions()
            .Where(xyc => xyc.c != '.')
            .GroupBy(xyc => xyc.c)
            .ToDictionary(g => g.Key, g => g.Select(xyc => xyc.position).ToList());
        
        var grid = new Grid
        {
            Size = input.GetGridSize(),
            Frequencies = frequencies
        };

        return grid;
    }
}