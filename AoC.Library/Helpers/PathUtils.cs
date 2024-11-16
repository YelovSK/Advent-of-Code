namespace AoC.Library.Helpers;

public static class PathUtils
{
    public static string GetBaseDirectory()
    {
        var currentDir = AppContext.BaseDirectory;

        var baseDir = Directory.GetParent(currentDir);
        baseDir = baseDir.Parent;
        baseDir = baseDir.Parent;
        baseDir = baseDir.Parent;

        return baseDir.FullName;
    }
}