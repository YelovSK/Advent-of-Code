using AoC.Library;
using AoC.Library.Helpers;

namespace AoC.Day06;

public class Day06 : BaseDay
{
    protected override string Part1(string input)
    {
        var map = GetMap(input);
        while (map.Guard.X > 0 && map.Guard.X < map.Size.Item2 - 1 && map.Guard.Y > 0 && map.Guard.Y < map.Size.Item1 - 1)
        {
            var next = map.Guard.GetNextPosition();
            if (map.Obstacles.Contains(next))
            {
                map.Guard.TurnRight();
            }
            
            map.Guard.Move();
        }

        return map.Guard.Positions.Count.ToString();
    }

    // Slow
    protected override string Part2(string input)
    {
        var map = GetMap(input);
        var loops = 0;
        
        foreach (var dot in map.Points)
        {
            map.Obstacles.Add(dot);

            while (map.Guard.X > 0 && map.Guard.X < map.Size.Item2 - 1 && map.Guard.Y > 0 && map.Guard.Y < map.Size.Item1 - 1)
            {
                if (map.Obstacles.Contains(map.Guard.GetNextPosition()))
                {
                    map.Guard.TurnRight();
                }
                
                if (!map.Guard.Move())
                {
                    loops++;
                    break;
                }
            }

            map.Obstacles.Remove(dot);
            map.Guard.Reset();
        }

        return loops.ToString();
    }

    protected override string RelativeInputPath => "Day06/input.txt";

    private Map GetMap(string input)
    {
        var lines = input.SplitLines().ToList();
        var map = new Map { Size = (lines.Count, lines.First().Length) };
        
        for (var y = 0; y < lines.Count; y++)
        {
            for (var x = 0; x < lines[y].Length; x++)
            {
                var c = lines[y][x];
                switch (c)
                {
                    case '#':
                        map.Obstacles.Add(new Point(x, y));
                        break;
                    case '.':
                        map.Points.Add(new Point(x, y));
                        break;
                    default:
                        if (map.Guard != null) throw new Exception("Multiple guards");
                        map.Guard = new Guard(c, x, y);
                        break;
                }
            }
        }

        return map;
    }
}