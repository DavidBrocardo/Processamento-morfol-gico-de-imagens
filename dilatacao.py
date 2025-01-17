import cv2
import numpy as np

def Dilatacao(img_binaria, elemento_Estruturante):
    bin_linhas = len(img_binaria) 
    bin_colunas = len(img_binaria[0]) 

    est_linhas = len(elemento_Estruturante) 
    est_colunas = len(elemento_Estruturante[0]) 
    # Determinar o deslocamento do kernel
    deslocamento_x  = est_linhas // 2
    deslocamento_y  = est_colunas // 2
    

    
    img_dilatacao = []
    for _ in range(bin_linhas):
        img_dilatacao.append([0] * bin_colunas)

    
    for i in range(deslocamento_x , bin_linhas - deslocamento_x ):
        for j in range(deslocamento_y, bin_colunas - deslocamento_y):
            
            regiao = img_binaria[i - deslocamento_x :i + deslocamento_x  + 1, j - deslocamento_y:j + deslocamento_y + 1]
           
            lin = len(regiao) 
            col = len(regiao[0]) 
            #print(regiao)
            controle = False
            for k in range (lin):
                for l in range (col):   
                    if regiao[k][l] != 0:    
                        #print("aqui")                    
                        controle = True   
            
            if(controle):
                img_dilatacao[i][j]= 255
            else:
                img_dilatacao[i][j] = 0 
                

    return img_dilatacao


def main(): 
    img_cinza = cv2.imread("img_erodida.png", cv2.IMREAD_GRAYSCALE)
    _, img_binaria = cv2.threshold(img_cinza, 127, 255, cv2.THRESH_BINARY)
    
    elemento_Estruturante = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    

    img_dilatacao = Dilatacao(img_binaria, elemento_Estruturante)

    img_dilatacao_np = np.array(img_dilatacao, dtype=np.uint8)
    cv2.imwrite("img_dilatacao.png", img_dilatacao_np)

    cv2.waitKey(0)
    #cv2.destroyAllWindows()
if __name__ == "__main__":
    main()