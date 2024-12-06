namespace AoC.Library.Helpers
{
    public static class Directions
    {
        public static readonly (int X, int Y) Up = (0, -1);
        public static readonly (int X, int Y) Down = (0, 1);
        public static readonly (int X, int Y) Left = (-1, 0);
        public static readonly (int X, int Y) Right = (1, 0);

        public static (int X, int Y) RotateRight((int X, int Y) direction)
        {
            if (direction == Up) return Right;
            if (direction == Right) return Down;
            if (direction == Down) return Left;
            if (direction == Left) return Up;
            throw new Exception($"Unknown direction {direction}");
        }

        public static (int X, int Y) RotateLeft((int X, int Y) direction)
        {
            if (direction == Up) return Left;
            if (direction == Right) return Up;
            if (direction == Down) return Right;
            if (direction == Left) return Down;
            throw new Exception($"Unknown direction {direction}");
        }
    }
}
