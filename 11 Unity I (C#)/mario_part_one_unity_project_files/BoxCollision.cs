using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class BoxCollision : MonoBehaviour
{
    public TextMeshProUGUI collisionText; 
    private Rigidbody2D rb;
    // Start is called before the first frame update
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }
    void OnCollisionEnter2D(Collision2D collision)
    {
        collisionText.text = "Collision";
        // Print a message to the Console when a 2D collision occurs
        Debug.Log("Csollided with: " + collision.gameObject.name);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
