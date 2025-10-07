import java.util.Scanner;

public class App {
    static Scanner sc = new Scanner(System.in);

    // ==================================== ATIVIDADE 1 ====================================
    public static void atividade1() {
        // Declaração de uma variável inteira chamada 'num'
        int num;
    
        // Lê um número inteiro da entrada do usuário usando o objeto 'sc' (Scanner)
        System.out.println("ATIVIDADE 1\n");
        System.out.print("Número: ");
        num = sc.nextInt();
        
        // Loop externo que itera de 1 até o valor de 'num' (inclusive)
        for (int i = 1; i <= num; i++) {
            // Imprime uma nova linha para começar uma nova sequência
            System.out.println("");
            
            // Loop interno que itera de 1 até o valor atual de 'i' (inclusive)
            for (int i2 = 1; i2 <= i; i2++) {
                // Imprime o valor de 'i2' seguido de um espaço, sem quebrar a linha
                System.out.print(i2 + " ");
            }
        }
        
        // Imprime uma nova linha ao final para garantir que o cursor fique na linha seguinte
        System.out.println("\n");
    }
    
    // ==================================== ATIVIDADE 2A ====================================
    public static void atividade2a() {
        // Declaração de uma variável inteira chamada 'num'
        int num;
    
        // Lê um número inteiro da entrada do usuário usando o objeto 'sc' (Scanner)
        System.out.println("ATIVIDADE 2B\n");
        System.out.print("Largura da bandeira: ");
        num = sc.nextInt();
        
        String[][] texts = new String[(num/2)+1][2];

        texts[0][0] = "";
        texts[0][1] = "";
        for (int i = 1; i <= num; i++) {
            texts[0][1] += "* ";
        }

        int index = 0;
        for (int i = num-1; i > 1; i=i-2) {
            index++;
            texts[index][0] = texts[index-1][0] + "  ";
            texts[index][1] = texts[index-1][1].substring(0, texts[index-1][1].length()-4);
        }

        System.out.println("");
        for (int i = index; i > 0; i--) {
            System.out.println(texts[i][0] + texts[i][1]);
        } 
        for (int i = 0; i <= index; i++) {
            System.out.println(texts[i][0] + texts[i][1]);
        }
        System.out.println("");
    }

    // ==================================== ATIVIDADE 2B ====================================    
    public static void atividade2b() {
        int num;
    
        System.out.println("ATIVIDADE 2B\n");
        System.out.print("Número: ");
        num = sc.nextInt();

        
        for (int i = num; i >= 1; i--) {
            System.out.println("");
            
            for (int i2 = 1; i2 <= i; i2++) {
                System.out.print("* ");
            }
        }
        
        System.out.println("\n");
    }
    
    // ==================================== ATIVIDADE 3 ====================================    
    public static void atividade3() {
        double nota;
        int alunos;
        int somar = 0;

        double maiorNota = 0;
        double menorNota = 0;
        String alunoMaior = "";
        String alunoMenor = "";

        System.out.println("São quantos alunos? ");
        alunos = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < alunos; i++){
        System.out.println("Nome do aluno:");
        String nome = sc.nextLine();

        System.out.println("Nota do aluno:");
        nota = sc.nextInt();
        sc.nextLine();

        somar += nota;

        if (i == 0) {

            maiorNota = nota;
            menorNota = nota;
            alunoMaior = nome;
            alunoMenor = nome;
        } else{
            if (nota > maiorNota){
                maiorNota = nota;
                alunoMaior = nome;
            }

            if (nota <menorNota) {
                menorNota = nota;
                alunoMenor = nome;
                
            }
        }

        }

        double media = somar/alunos;

        System.out.println("A média da turma foi: " + media + " de um total de " + alunos + " alunos.");
        System.out.println();
        System.out.println("O aluno com a maior nota foi o " + alunoMaior + " com uma nota de " + maiorNota);
        System.out.println();
        System.out.println("O aluno com a menor nota foi o " + alunoMenor + " com uma nota de " + menorNota);

    }

    public static void main(String[] args) throws Exception {
        App.atividade1();
        App.atividade2a();
        App.atividade2b();
        // App.atividade2c();
        App.atividade3();
    }
}