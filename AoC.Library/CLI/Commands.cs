using AoC.Library.Helpers;
using System.Reflection;

namespace AoC.Library.CLI
{
    public static class Commands
    {
        public static void RunDay(SolveOptions options, Assembly assembly)
        {
            options.Day ??= GetLatestDay();
            var className = $"AoC.Day{options.Day:D2}.Day{options.Day:D2}";

            var dayType = assembly.GetType(className);
            if (dayType == null)
            {
                Console.WriteLine($"Solution class for Day {options.Day:D2} not found: {className}");
                return;
            }

            if (Activator.CreateInstance(dayType) is not BaseDay day)
            {
                Console.WriteLine($"Day {options.Day:D2} does not inherit {nameof(BaseDay)}.");
                return;
            }

            var result = Solver.Solve(day, new Library.SolveOptions(options.Part1, options.Part2));
            Console.WriteLine(result);
        }

        public static void CreateDayFolder(CreateOptions options)
        {
            options.Day ??= GetLatestDay();
            var day = options.Day;

            var folderName = Path.Combine(PathUtils.GetBaseDirectory(), $"Day{day:D2}");
            if (Directory.Exists(folderName))
            {
                Console.WriteLine($"Folder for Day {day:D2} already exists.");
                return;
            }

            Directory.CreateDirectory(folderName);

            File.WriteAllText($"{folderName}/Day{day:D2}.cs", GenerateDayTemplate(day.Value));
            File.Create($"{folderName}/input.txt").Close();

            Console.WriteLine($"Folder for Day {day:D2} created.");
        }

        public static int GetLatestDay()
        {
            return Directory.GetDirectories(PathUtils.GetBaseDirectory(), "Day*")
                .Select(path => int.Parse(path[^2..]))
                .Max();
        }

        public static string GenerateDayTemplate(int day)
        {
            return $$"""
             using AoC.Library;

             namespace AoC.Day{{day:D2}};

             public class Day{{day:D2}} : BaseDay
             {
                 protected override string Part1(string input)
                 {
                     throw new NotImplementedException();
                 }
             
                 protected override string Part2(string input)
                 {
                     throw new NotImplementedException();
                 }
             
                 protected override string RelativeInputPath => "Day{{day:D2}}/input.txt";
             }
             """;
        }
    }
}
