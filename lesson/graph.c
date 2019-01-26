//
//  main.c
//  graph
//
//  Created by Rebecca on 2019/1/11.
//  Copyright © 2019 Rebecca. All rights reserved.
//

#include "main.h"
#include<stdio.h>
#include<stdlib.h>
#define MaxVex 100
int visited[MaxVex];  //全局数组,用于记录图中节点访问状态
typedef struct EdgeNode { //邻接表节点
    int adjvex;    //该邻接点在顶点数组中的下标
    struct EdgeNode *next;   //指向下一个邻接点
}EdgeNode;

typedef struct VertexNode { //头节点
    char data;  //顶点信息
    EdgeNode *firstedge;  //邻接表头指针(指向第一条依附于该顶点的弧的指针)
}VertexNode,AdjList[MaxVex]; //顶点数组(结构体数组)

typedef struct Graph{//邻接表
    AdjList adjList;//存顶点的数组
    int numVertexes,numEdges;  //图中当前的结点数以及边数
}Graph,*GraphAdjList;

//建立无向图的邻接表结构
void CreateALGraph(GraphAdjList &G){
    int i, j, k;
    if(G==NULL)
        G = (GraphAdjList)malloc(sizeof(Graph));
    
    printf("输入图的结点数以及边数: ");
    scanf("%d%d",&G->numVertexes,&G->numEdges);
    fflush(stdin);
    
    printf("===========================\n");
    printf("输入各个顶点的数据:\n");
    for (i=0; i<G->numVertexes; ++i){
        printf("顶点%d: ",i);
        scanf("%c", &(G->adjList[i].data));//将顶点数据放入数据域
        G->adjList[i].firstedge = NULL;//边表头指针初始为NULL
        fflush(stdin);
    }
    
    printf("===========================\n");
    for (k=0; k<G->numEdges; ++k){ //输入边的信息并与顶点建立联系
        printf("输入(vi,vj)上的顶点序号: ");
        scanf("%d%d",&i,&j);
        
        EdgeNode *ptrEdgeNode = (EdgeNode*)malloc(sizeof(EdgeNode));
        ptrEdgeNode->adjvex = j; //边节点数据域存顶点下标
        ptrEdgeNode->next = G->adjList[i].firstedge;//表头后面插入边节点
        G->adjList[i].firstedge = ptrEdgeNode;
        
        ptrEdgeNode = (EdgeNode*)malloc(sizeof(EdgeNode));
        ptrEdgeNode->adjvex = i; //无向图再进行一次相反操作
        ptrEdgeNode->next = G->adjList[j].firstedge;
        G->adjList[j].firstedge = ptrEdgeNode;
    }
}

/** 堆栈定义及相关操作(深度优先遍历会用到此栈) **/
int Stack[MaxVex];
int Stackcount=-1;//堆栈指针

int StackEmpty(){//判断栈空
    return Stackcount==-1;
}

int StackFull(){//判断栈满
    return Stackcount==MaxVex-1;
}

void Push(int e){//入栈
    if(!StackFull())
        Stack[++Stackcount]=e;
    else
        printf("Full");
}

void Pop(){//出栈
    if(!StackEmpty())
        Stackcount--;
    else
        printf("Empty");
}
/*************************************************/

void DFS1Traverse(GraphAdjList &G){ //深度优先遍历(堆栈实现)
    int i;
    for (i=0; i<G->numVertexes; ++i)
        visited[i]=0;//初始化访问状态
    i=0;//从i号顶点开始遍历
    visited[i] = 1;
    printf("%c ", G->adjList[i].data);
    Push(i);//将起始节点进栈，以便将来正确返回
    while(!StackEmpty())
    {
        EdgeNode *p=G->adjList[Stack[Stackcount]].firstedge;//指向栈顶元素的邻接表头
        while(p)//
        {
            if(!visited[p->adjvex])//若当前邻接顶点没有被访问过，则进行访问并入栈
            {
                printf("%c ",G->adjList[p->adjvex].data);
                visited[p->adjvex]=1;
                Push(p->adjvex);//访问顶点进栈
                break;
            }
            else//若当前邻接顶点已经被访问过，则沿边找到下一个顶点
                p=p->next;
        }
        if(p==NULL)//若某一方向被访问完，则回溯寻找未被访问的顶点
            Pop();
    }
}
void DFS2(GraphAdjList &G, int i){ //递归深度优先遍历(递归实现)
    visited[i] = 1;//改变访问状态
    printf("%c ",G->adjList[i].data);//输出顶点
    
    EdgeNode *p=G->adjList[i].firstedge;
    while(p){
        if(!visited[p->adjvex])//若节点尚未访问
            DFS2(G,p->adjvex); //递归深度遍历
        p=p->next;//边节点指针后移
    }
}

void DFS2Traverse(GraphAdjList &G){
    int i;
    for (i=0; i<G->numVertexes;++i)
        visited[i] = 0;  //初始化访问数组visited的元素值为0
    
    for (i=0; i<G->numVertexes;++i){
        if(!visited[i]) //节点尚未访问
            DFS2(G,i); //调用遍历函数
    }
}
/** 队列定义及相关操作(广度优先遍历会用到此循环队列) **/
int Queue[MaxVex];
int front=0,rear=0;//队头和队尾指针

int QueueEmpty(){
    return front == rear;
}

int QueueFull(){
    return rear == MaxVex-1;
}

void EnQueue(int e){//队尾插入元素
    if(!QueueFull())
        Queue[rear++] = e;
}

void DeQueue(int *e){//队头删除元素
    if(!QueueEmpty())
        *e = Queue[front++];
}
/*************************************************/

void BFSTraverse(GraphAdjList &G){//图的广度优先遍历
    int i;
    for (i=0; i<G->numVertexes; ++i)
        visited[i] = 0;//初始化访问状态
    i=0;//从i号顶点开始遍历
    visited[i] = 1;
    printf("%c ", G->adjList[i].data);
    EnQueue(i);
    
    while (!QueueEmpty())
    {
        DeQueue(&i);
        EdgeNode *p = G->adjList[i].firstedge;//指向队头元素的邻接表头
        while (p)
        {
            if (!visited[p->adjvex])//若当前邻接顶点没有被访问过，则进行访问并入队
            {
                visited[p->adjvex] = 1;
                printf("%c ", G->adjList[p->adjvex].data);
                EnQueue(p->adjvex);
            }
            p = p->next;//访问下一个相连的顶点
        }
    }
}

//邻接表输出
void ShowVlist(GraphAdjList &G){
    int i;
    EdgeNode* curp;
    
    printf("===========================\n邻接表输出:\n");
    for(i=0;i<G->numVertexes;i++)
    {
        printf("\%c",G->adjList[i].data);
        curp=G->adjList[i].firstedge;//边节点指针指向第一个边节点
        while(curp!=NULL)
        {
            printf("-->%d",curp->adjvex);
            curp=curp->next;//依次往后遍历
        }
        printf("\n");
    }
}

int main()
{
    GraphAdjList G = NULL;
    CreateALGraph(G);//创建邻接表
    ShowVlist(G);//输出邻接表
    
    printf("\n图的深度优先遍历(堆栈实现)为:\t");
    DFS1Traverse(G);
    
    printf("\n图的深度优先遍历(递归实现)为:\t");
    DFS2Traverse(G);
    
    printf("\n图的广度优先遍历为:\t\t");
    BFSTraverse(G);
    
    printf("\n\n");
    return 0;
}

