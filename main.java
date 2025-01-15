class Project {
    public String name;

    public Project(String name) {
        this.name = name;
    }

    public void compile(String projectName) {
        System.out.println("Project " + projectName + " compiled.");
    }

    public void compile() {
        compile(this.name);
    }
}

public class main {
    public static void main(String[] args) {
        Project project1 = new Project("project1");
        Project project2 = new Project("project2");
        project2.name = "test_for_project2";
        project1.compile();
        project2.compile();
    }
}
