namespace AoC.Day06;

public class Guard
{
    public int X { get; private set; }
    public int Y { get; private set; }
    public (int, int) Direction { get; private set; }
    public readonly HashSet<GuardState> Positions = [];
    
    // Original
    private readonly (int, int) _direction;
    private readonly int _x;
    private readonly int _y;

    public Guard(char c, int x, int y)
    {
        X = x;
        Y = y;

        Direction = c switch
        {
            '^' => (0, -1),
            'v' => (0, 1),
            '<' => (-1, 0),
            '>' => (1, 0),
            _ => throw new ArgumentOutOfRangeException()
        };
        Positions.Add(new GuardState(new Point(x, y), Direction));
        
        _direction = Direction;
        _x = x;
        _y = y;
    }

    public void Reset()
    {
        X = _x;
        Y = _y;
        Direction = _direction;
        Positions.Clear();
    }

    public bool Move()
    {
        X += Direction.Item1;
        Y += Direction.Item2;
        return Positions.Add(new GuardState(new Point(X, Y), Direction));
    }
    
    public Point GetNextPosition() => new(X + Direction.Item1, Y + Direction.Item2);

    public void TurnRight()
    {
        Direction = Direction switch
        {
            (0, -1) => (1, 0),
            (0, 1) => (-1, 0),
            (-1, 0) => (0, -1),
            (1, 0) => (0, 1),
            _ => throw new ArgumentOutOfRangeException()
        };
    }

    public override string ToString()
    {
        return $"{X}, {Y}";
    }
}